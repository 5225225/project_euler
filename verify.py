import sys
import subprocess
import base64

def verify(prog, timeout=60):
    result = int(subprocess.check_output(
        "./{}".format(prog),
        timeout=timeout,
    ).strip())

    if result == results[prog]:
        return True
    else:
        print("=== Error in program {}".format(prog))
        print("Got:      {}".format(result))
        print("Expected: {}".format(results[prog]))
        return False
        

results = {}

with open("answers.txt") as f:
    for line in f:
        prog, answer = line.split("|")
        prog = prog.strip()
        answer = int(base64.b64decode(answer.strip()))

        results[prog] = answer

failed = [prog for prog in results if not verify(prog)]

sys.exit(min(len(failed), 255))
