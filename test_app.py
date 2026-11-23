import subprocess
import sys

from app import main


def test_main_prints_greeting(capsys):
    main()
    output = capsys.readouterr().out
    assert "Hello, Jenkins!" in output


def test_main_prints_one_line(capsys):
    main()
    output = capsys.readouterr().out
    assert len(output.strip().splitlines()) == 1


def test_main_returns_nothing():
    assert main() is None


def test_running_script_directly_works():
    result = subprocess.run([sys.executable, "app.py"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Hello, Jenkins!" in result.stdout