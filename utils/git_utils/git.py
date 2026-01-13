import subprocess

def get_git_commit():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"]
        ).decode().strip()
    except Exception:
        return "not_a_git_repo"
    
def get_git_branch():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"]
        ).decode().strip()
    except Exception:
        return "unknown"
    
def git_is_dirty():
    try:
        status = subprocess.check_output(
            ["git", "status", "--porcelain"]
        ).decode().strip()
        return bool(status)
    except Exception:
        return None