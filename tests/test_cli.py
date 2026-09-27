import subprocess
import sys


def run_cli(*args):
    return subprocess.run(
        [sys.executable, "-m", "toolkit", *args],
        capture_output=True,
        text=True,
        check=False,
    )


def test_cli_1():
    result = run_cli("calc", "2+3*4")
    assert result.returncode == 0
    assert result.stdout.strip() == "14"


def test_cli_2():
    result = run_cli("calc", "2*/3")
    assert result.returncode == 2
    assert result.stderr != ""


def test_cli_3():
    result = run_cli("--help")
    assert result.returncode == 0
