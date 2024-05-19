
import os
import fitz  # PyMuPDF
import psycopg2
import re


# Function to establish a connection to PostgreSQL
def connect_to_database():
    conn = psycopg2.connect(
        dbname="Skill",
        user="postgres",
        password="123",
        host="localhost",
        port="5432"
    )
    return conn


# Function to insert data into the database
def insert_into_database(conn, file_name, extracted_skills):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Skills (file_name, extracted_skills) VALUES (%s, %s)",
                       (file_name, extracted_skills))
        conn.commit()
        print("Data inserted into database for file:", file_name)
    except psycopg2.Error as e:
        conn.rollback()
        print("Error inserting data for file:", file_name, "Error:", e)
    finally:
        cursor.close()


# Function to extract skills from a PDF using regular expressions
def extract_skills_from_pdf(pdf_path):
    extracted_skills = ""
    pattern = r'(?i)(?:Skills?|Proficiencies?|Competencies?)\s*:?([\s\S]*?)(?=\n\n|\n[A-Z])'

    with fitz.open(pdf_path) as doc:
        for page in doc:
            page_text = page.get_text()
            match = re.search(pattern, page_text)
            if match:
                extracted_skills = match.group(1).strip()
                break

    return extracted_skills


# Function to process PDF files in a directory
def process_pdfs_in_directory(directory_path, conn):
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory_path, filename)
            print("Processing:", pdf_path)
            extracted_skills = extract_skills_from_pdf(pdf_path)
            if extracted_skills:
                insert_into_database(conn, filename, extracted_skills)
            else:
                print("No skills found in the PDF:", filename)
            print()  # Add an empty line for better readability between PDFs


def main():
    directory_path = r'C:\Users\Sayali\Downloads\Resume\Resume'  # Provide the directory path here

    conn = connect_to_database()
    process_pdfs_in_directory(directory_path, conn)
    conn.close()

if __name__ == "__main__":
    main()