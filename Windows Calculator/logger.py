import json
import os
import inspect
from datetime import datetime

LOG_FOLDER = "Test Run Logs"  
HTML_FILE = "recent_test_results.html"  

def get_log_filename():
    """Generate a log filename with the current date and store it in the 'Test Run Logs' folder."""
    current_date = datetime.now().strftime("%Y-%m-%d")
    os.makedirs(LOG_FOLDER, exist_ok=True)  
    return os.path.join(LOG_FOLDER, f"test_results_{current_date}.json")

def log_test_result(test_name, status, expected_result, actual_result=None):
    """Log the test result to a date-stamped JSON file inside the 'Test Run Logs' folder."""
    result_data = {
        "test_name": test_name,
        "status": status,
        "expected_result": expected_result,
        "actual_result": actual_result,
        "timestamp": datetime.now().isoformat()
    }
    
    log_filename = get_log_filename()

    try:
        with open(log_filename, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    
    data.append(result_data)
    
    with open(log_filename, "w") as f:
        json.dump(data, f, indent=4)

    generate_html_report()

def log_result(expected_result, actual_result):
    """Log the result of a test based on the expected and actual result."""
    test_name = inspect.stack()[1].function

    if expected_result == actual_result:
        log_test_result(test_name, "pass", expected_result)
    else:
        log_test_result(test_name, "fail", expected_result, actual_result)

def generate_html_report():
    """Generate an HTML report of the most recent test results."""
    log_filename = get_log_filename()
    
    try:
        with open(log_filename, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []


    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    html_content = f"""
    <html>
    <head><title>Recent Test Results</title></head>
    <body>
    <h1>Most Recent Test Results</h1>
    <p><strong>Generated on:</strong> {timestamp}</p>
    <ul>
    """
    
    # Automatically determine the number of results based on the number of tests in the log
    # If there are fewer than 5 tests, show all of them
    results_to_show = len(data) if len(data) < 5 else 5
    
    recent_results = data[-results_to_show:]
    
    # Reverse the order of the entries to show oldest first
    recent_results.reverse()
    
    for result in recent_results:
        # Set color based on status
        if result['status'] == 'pass':
            color = "green"
        else:
            color = "red"
        
        # Add timestamp for each test entry
        test_timestamp = result['timestamp']
        
        html_content += f"""
        <li style="color:{color};">
            <strong>{result['test_name']}</strong>: {result['status'].capitalize()}
            <br><em>Timestamp: {test_timestamp}</em>
        </li>
        """
    
    html_content += """
    </ul>
    </body>
    </html>
    """
    
    with open(os.path.join(LOG_FOLDER, HTML_FILE), "w") as f:
        f.write(html_content)
