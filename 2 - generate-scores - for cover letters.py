from common import load_file_text, write_file


prompt = """
your name is Jan and you are a hiring manager at Thankyou payroll. 
You are hiring for the following position. """ + load_file_text("inputs/1-job.txt") + """
\n------------------------------\n
evaluate following cover letters for the position.
give a score and justification. \n\n """ + load_file_text("inputs/2-coverletters.txt")

filename = 'output/2-prompt-for-scoring.txt'
write_file(filename, prompt)

print(" file printed to " + filename)