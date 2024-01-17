import subprocess

subprocess.run(["docker", "build", "-t", "microservicio", "."])

subprocess.run(["docker", "run",  "-d","-p", "8000:8000", "microservicio"])
