

from common import load_file_text, write_file


messages="""
read my experiance below.
\n
""" + load_file_text("experiance.txt") + "\n" + """
--------------------------------------------------------------\n
following is the job posting I am trying to apply. \n
""" + load_file_text("inputs/1-job.txt") + "\n" + """
--------------------------------------------------------------\n
write me three cover letters for this job posting. 
- if you can find the name of the hiring manager, please use it, if not address the team at the company.
- do not mention C# unless it is requred in the job posting.
- do not mention React unless it is requred in the job posting.
- cover letter will be submitted via a web form.
- split the cover letters by a line of hashes.
"""

file = 'output/1-prompt-for-cover-letters.txt'
write_file(file,messages)


print(" file printed to " + file)

messages="""
read my experiance below.
\n
""" + load_file_text("experiance.txt") + "\n" + """
--------------------------------------------------------------\n
following is the job posting I am trying to apply. \n
""" + load_file_text("inputs/1-job.txt") + "\n" + """
--------------------------------------------------------------\n
write me three CVs in MD format for this job posting. 
- do not include the personal Details section, I will fill that in myself.
"""

file = 'output/1-prompt-for-CV.txt'
write_file(file,messages)



print(" file printed to " + file)
# response.choices[0].text)
