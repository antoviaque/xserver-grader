def grade(grader_path, grader_config, student_response, sandbox):
    print grader_path, grader_config, student_response, sandbox
    
    results = {
        'correct': True,
        'score': 1,
        'tests': [],
        'errors': []
    }
    return results
