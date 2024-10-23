from main import dict

body_start = """
<!DOCTYPE html>
<html>
<head>
</head>
    <body>
        <h1 style="text-decoration: underline black">Las news:</h1>
        <p></p>
"""
content = []
for key,value in dict.items():
    x = """
    <a style="color: #000000" href="""+value+">"+key+"</a><br/><br/>"
    content.append(x)

body_end = """
    </body>
</html>
"""

mailBody = body_start + ''.join(content) + body_end