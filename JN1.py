import os
import fitz  # PyMuPDF

# Define the keywords for each job role
job_keywords = {
    "Java Developer": ["Java", "Spring Framework", "Hibernate", "RESTful", "Git", "J2EE", "MVC Architecture", "SQL", "Agile", "Unit Testing"],
    "Python Developer": ["Python", "Django", "Flask", "Pandas", "Git", "RESTful", "SQL", "Automated Testing", "Data Analysis", "Agile"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "jQuery", "Git", "Bootstrap", "PHP", "MySQL", "MVC Architecture"],
    "Frontend Developer": ["HTML", "CSS", "JavaScript", "Bootstrap", "Git", "AngularJS", "ReactJS", "Vue.js", "Responsive Design"],
    "Backend Developer": ["Node.js", "Express.js", "SQL", "MongoDB", "Git", "RESTful", "NoSQL", "MVC Architecture"],
    "Full Stack Developer": ["HTML", "CSS", "JavaScript", "Node.js", "Express.js", "SQL", "Git", "MVC Architecture", "RESTful", "Agile", "Unit Testing"],
    "Software Engineer": ["Programming Languages", "Algorithms", "OOP", "Git", "Agile", "Software Development Life Cycle", "Design Patterns", "Data Structures", "Unit Testing"],
    "DevOps Engineer": ["Linux", "Docker", "Jenkins", "AWS", "Git", "Kubernetes", "Continuous Integration", "Infrastructure as Code", "Monitoring", "Scripting"],
    "Database Developer": ["SQL", "Database Development", "Stored Procedures", "Indexes", "ETL", "Data Modeling", "Database Optimization", "Query Optimization", "Database Design"],
    "Data Engineer": ["Data Engineering", "ETL", "SQL", "Big Data", "Data Warehousing", "Hadoop", "Spark", "Data Modeling", "Data Integration"],
    "Business Intelligence (BI) Developer": ["Business Intelligence", "Tableau", "SQL", "Data Visualization", "ETL", "BI Tools", "Dashboard Development", "Reporting"],
    "ETL Developer": ["ETL", "Data Integration", "Informatica", "SQL", "Scripting", "Data Warehousing", "Data Transformation", "Data Loading"],
    "Data Analyst": ["Data Analysis", "SQL", "Data Visualization", "BI Tools", "Python", "Statistical Analysis", "Data Mining", "Excel"],
    "Big Data Engineer": ["Big Data", "Hadoop", "Spark", "NoSQL", "Scala", "Data Engineering", "Data Processing", "MapReduce", "Distributed Systems"],
    "Cloud Developer": ["Cloud Computing", "AWS", "Microservices", "Docker", "Kubernetes", "Serverless Architecture", "Infrastructure as Code", "Scalability"],
    "Game Developer": ["Game Development", "Unity", "C#", "3D Modeling", "Game Design", "Game Engine", "Physics Engine", "Virtual Reality"],
    "Mobile App Developer": ["Mobile Development", "iOS", "Android", "Swift", "Kotlin", "Xamarin", "Flutter", "Mobile UI/UX", "RESTful APIs"],
    "Embedded Systems Developer": ["Embedded Systems", "Firmware Development", "RTOS", "Microcontrollers", "Hardware Interfacing", "Embedded C", "ARM Cortex", "Embedded Linux"],
    "UI/UX Designer": ["UI Design", "UX Design", "Wireframing", "Prototyping", "Adobe XD", "Sketch", "User Research", "User Testing", "Responsive Design", "Mobile UI/UX"],
    "Quality Assurance (QA) Automation Engineer": ["Test Automation", "Selenium WebDriver", "Continuous Integration", "Test Automation Frameworks", "Jenkins", "TestNG", "JUnit", "BDD", "Cucumber"],
    "Blockchain Developer": ["Blockchain", "Ethereum", "Smart Contracts", "Cryptography", "Decentralized Applications (DApps)", "Web3.js", "Truffle", "Solidity"],
    "AR/VR Developer": ["Augmented Reality", "Virtual Reality", "Unity3D", "ARKit", "ARCore", "Game Development", "3D Modeling", "VR Development"],
    "Machine Learning Engineer": ["Machine Learning", "Deep Learning", "TensorFlow", "Neural Networks", "Data Science", "AI", "Model Deployment", "Python"],
    "Natural Language Processing (NLP) Engineer": ["Natural Language Processing", "NLP", "Text Mining", "NLTK", "SpaCy", "Word Embeddings", "Sentiment Analysis", "Named Entity Recognition"]
}

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.

    Args:
    - pdf_path (str): Path to the PDF file.

    Returns:
    - str: Text extracted from the PDF.
    """
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_keywords_from_resume(resume_text):
    """
    Extract keywords from the resume text.

    Args:
    - resume_text (str): Text extracted from the resume.

    Returns:
    - list of str: Keywords extracted from the resume.
    """
    # For simplicity, let's assume keywords are separated by spaces in the resume text
    return resume_text.split()

def calculate_score(resume_keywords, job_keywords):
    """
    Calculate the score for the resume based on matched job keywords.

    Args:
    - resume_keywords (list of str): Keywords extracted from the resume.
    - job_keywords (list of str): Keywords relevant to the job description.

    Returns:
    - float: Score out of 5 based on the matched keywords.
    """
    matched_keywords = set(resume_keywords) & set(job_keywords)
    score = len(matched_keywords) / len(job_keywords) * 5
    return score

def match_job_roles(resume_keywords):
    """
    Match resume keywords with predefined job keywords and calculate the scores.

    Args:
    - resume_keywords (list of str): Keywords extracted from the resume.

    Returns:
    - dict: Dictionary containing matching job roles and their scores.
    """
    scores = {}
    for job_role, job_role_keywords in job_keywords.items():
        score = calculate_score(resume_keywords, job_role_keywords)
        scores[job_role] = score
    return scores

def process_resumes_in_directory(directory_path):
    """
    Process all resumes in a directory and determine the matching job roles.

    Args:
    - directory_path (str): Path to the directory containing resume files.
    """
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            resume_path = os.path.join(directory_path, filename)
            resume_text = extract_text_from_pdf(resume_path)
            resume_keywords = extract_keywords_from_resume(resume_text)
            scores = match_job_roles(resume_keywords)
            sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
            print(f"Resume '{filename}':")
            for job_role, score in sorted_scores:
                print(f" - {job_role}: {score:.2f}/5")

if __name__ == "__main__":
    # Specify the directory path containing the resume files
    directory_path = r"C:\Users\Sayali\Downloads\Resume\Resume"
    process_resumes_in_directory(directory_path)
