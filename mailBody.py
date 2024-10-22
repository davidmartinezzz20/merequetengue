from main import dict

body_start = """
<html>
<head></head>
    <body>
        <p></p>
"""
content = []
for key,value in dict.items():
    x = """
    <a href="""+value+">"+key+"</a>"
    content.append(x)

body_end = """
    </body>
</html>
"""

mailBody = body_start.join(content) + body_end