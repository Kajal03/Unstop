"""
Lists all lambda functions along with corresponding API's HTTP method and folder name
HTTP method is set to None for functions which doesn't require APIs 
"""

LAMBDA_CONFIG = {'get-all-available-seats': {'folder': 'endpoints', 'http_method': 'GET', 'timeout_duration': 30}
                 }