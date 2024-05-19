import os
import fitz  # PyMuPDF


def find_words_and_text_in_pdf(pdf_path, words):
    """
    Find specific words and extract the text after the first occurrence of the largest word in the list.

    Args:
    - pdf_path (str): Path to the PDF document.
    - words (list of str): Words to search for in the PDF.

    Returns:
    - str: Text following the first occurrence of the largest word in the list, limited to 6-7 non-empty lines.
    """
    text_after_words = ""
    largest_word = ""

    with fitz.open(pdf_path) as doc:
        for page in doc:
            page_text = page.get_text()
            for word in sorted(words, key=len, reverse=True):
                if word in page_text:
                    idx = page_text.find(word)
                    if largest_word == "" or len(word) > len(largest_word):
                        largest_word = word
                        text_after_words = page_text[idx + len(word):].strip()
                        break  # Stop searching once the first match is found

    # Split the text into lines
    lines = text_after_words.split('\n')

    # Filter out empty lines and limit to 6-7 non-empty lines
    non_empty_lines = [line for line in lines if line.strip()]
    limited_lines = non_empty_lines[:15]

    # Join the limited lines back into a single string
    limited_text = '\n'.join(limited_lines)

    return limited_text


def calculate_score(text, job_keywords):
    """
    Calculate the score for the resume based on matched job keywords.

    Args:
    - text (str): Text extracted from the resume.
    - job_keywords (list of str): Keywords relevant to the job description.

    Returns:
    - float: Score out of 10 based on the matched keywords.
    """
    score = 0
    for keyword in job_keywords:
        if keyword.lower() in text.lower():
            score += 1
    max_possible_score = len(job_keywords)
    if max_possible_score == 0:
        return 0  # Avoid division by zero
    normalized_score = (score / max_possible_score) * 10
    return normalized_score


def process_pdfs_in_directory(directory_path, job_keywords):
    """
    Process all PDF files in a directory and calculate scores based on job keywords.

    Args:
    - directory_path (str): Path to the directory containing PDF files.
    - job_keywords (list of str): Keywords relevant to the job description.
    """
    # Specify the words to search for, including variations with spaces
    words_to_find = [
        "Skills", "Skill", "Proficiencies", "Proficiency", "Competencies",
        "S K I L L S", "S K I L L S", "skill", "proficiencies", "proficiency", "competencies",
        "S K I L L S".replace(" ", ""), "skill".replace(" ", ""), "proficiencies".replace(" ", ""),
        "proficiency".replace(" ", ""), "competencies".replace(" ", "")
    ]

    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory_path, filename)
            print("Processing:", pdf_path)
            text_after_words = find_words_and_text_in_pdf(pdf_path, words_to_find)
            if text_after_words:
                print("Text after the matched words (limited to 6-7 lines without empty lines):")
                print(text_after_words)
                score = calculate_score(text_after_words, job_keywords)
                print("Score:", score)
            else:
                print("No text found after the matched words in the PDF.")
            print()  # Add an empty line for better readability between PDFs

if __name__ == "__main__":
    # Your main code here

    # Specify the directory path containing the PDF files
    directory_path = r"C:\Users\Prasen\Desktop\A\Python\Practice\100 test"

    # Dictionary containing job descriptions as keys and their related keywords as values
    job_descriptions = {
        "Java Developer": ["Java", "Spring Framework", "Hibernate", "RESTful", "Git", "J2EE", "MVC Architecture", "SQL",
                           "Agile", "Unit Testing"],
        "Python Developer": ["Python", "Django", "Flask", "Pandas", "Git", "RESTful", "SQL", "Automated Testing",
                             "Data Analysis", "Agile"],
        "Web Developer": ["HTML", "CSS", "JavaScript", "jQuery", "Git", "Bootstrap", "PHP", "MySQL",
                          "MVC Architecture"],
        "Frontend Developer": ["HTML", "CSS", "JavaScript", "Bootstrap", "Git", "AngularJS", "ReactJS", "Vue.js",
                               "Responsive Design"],
        "Backend Developer": ["Node.js", "Express.js", "SQL", "MongoDB", "Git", "RESTful", "NoSQL", "MVC Architecture"],
        "Full Stack Developer": ["HTML", "CSS", "JavaScript", "Node.js", "Express.js", "SQL", "Git", "MVC Architecture",
                                 "RESTful", "Agile", "Unit Testing"],
        "Software Engineer": ["Programming Languages", "Algorithms", "OOP", "Git", "Agile",
                              "Software Development Life Cycle", "Design Patterns", "Data Structures", "Unit Testing"],
        "DevOps Engineer": ["Linux", "Docker", "Jenkins", "AWS", "Git", "Kubernetes", "Continuous Integration",
                            "Infrastructure as Code", "Monitoring", "Scripting"],
        "Database Developer": ["SQL", "Database Development", "Stored Procedures", "Indexes", "ETL", "Data Modeling",
                               "Database Optimization", "Query Optimization", "Database Design"],
        "Data Engineer": ["Data Engineering", "ETL", "SQL", "Big Data", "Data Warehousing", "Hadoop", "Spark",
                          "Data Modeling", "Data Integration"],
        "Business Intelligence (BI) Developer": ["Business Intelligence", "Tableau", "SQL", "Data Visualization", "ETL",
                                                 "BI Tools", "Dashboard Development", "Reporting"],
        "ETL Developer": ["ETL", "Data Integration", "Informatica", "SQL", "Scripting", "Data Warehousing",
                          "Data Transformation", "Data Loading"],
        "Data Analyst": ["Data Analysis", "SQL", "Data Visualization", "BI Tools", "Python", "Statistical Analysis",
                         "Data Mining", "Excel"],
        "Big Data Engineer": ["Big Data", "Hadoop", "Spark", "NoSQL", "Scala", "Data Engineering", "Data Processing",
                              "MapReduce", "Distributed Systems"],
        "Cloud Developer": ["Cloud Computing", "AWS", "Microservices", "Docker", "Kubernetes",
                            "Serverless Architecture", "Infrastructure as Code", "Scalability"],
        "Game Developer": ["Game Development", "Unity", "C#", "3D Modeling", "Game Design", "Game Engine",
                           "Physics Engine", "Virtual Reality"],
        "Mobile App Developer": ["Mobile Development", "iOS", "Android", "Swift", "Kotlin", "Xamarin", "Flutter",
                                 "Mobile UI/UX", "RESTful APIs"],
        "Embedded Systems Developer": ["Embedded Systems", "Firmware Development", "RTOS", "Microcontrollers",
                                       "Hardware Interfacing", "Embedded C", "ARM Cortex", "Embedded Linux"],
        "UI/UX Designer": ["UI Design", "UX Design", "Wireframing", "Prototyping", "Adobe XD", "Sketch",
                           "User Research", "User Testing", "Responsive Design", "Mobile UI/UX"],
        "Quality Assurance (QA) Automation Engineer": ["Test Automation", "Selenium WebDriver",
                                                       "Continuous Integration", "Test Automation Frameworks",
                                                       "Jenkins", "TestNG", "JUnit", "BDD", "Cucumber"],
        "Blockchain Developer": ["Blockchain", "Ethereum", "Smart Contracts", "Cryptography",
                                 "Decentralized Applications (DApps)", "Web3.js", "Truffle", "Solidity"],
        "AR/VR Developer": ["Augmented Reality", "Virtual Reality", "Unity3D", "ARKit", "ARCore", "Game Development",
                            "3D Modeling", "VR Development"],
        "Machine Learning Engineer": ["Machine Learning", "Deep Learning", "TensorFlow", "Neural Networks",
                                      "Data Science", "AI", "Model Deployment", "Python"],
        "Natural Language Processing (NLP) Engineer": ["Natural Language Processing", "NLP", "Text Mining", "NLTK",
                                                       "SpaCy", "Word Embeddings", "Sentiment Analysis",
                                                       "Named Entity Recognition"]
    }

    # Prompt the user to choose a job description
    print("Choose a job description:")
    for idx, job_desc in enumerate(job_descriptions.keys(), 1):
        print(f"{idx}. {job_desc}")
    choice = int(input("Enter the number corresponding to your choice: "))
    selected_job_description = list(job_descriptions.keys())[choice - 1]
    job_keywords = job_descriptions[selected_job_description]

    # Process all PDF files in the directory and calculate scores
    process_pdfs_in_directory(directory_path, job_keywords)