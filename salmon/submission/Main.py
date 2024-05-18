import subprocess

def main():
    subprocess.call(['streamlit', 'run', 'submission/dashboard.py'])

if __name__ == "__main__":
    main()