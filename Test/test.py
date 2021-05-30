"""Script to automate test"""
import os
import subprocess
import datetime

"""Root folder in which scripts to be test is located"""
ROOT_DIR = "D:\\ironpythontest"


def write_log(data):
    """Writes log data to disk as csv file. Returns True when done

    @params data: string to be added to file
    """

    # add headers to csv if file doesn't exist
    if not os.path.exists(os.path.join(os.getcwd(), "log.csv")):
        with open(os.path.join(os.getcwd(), "log.csv"), "w+") as file:
            file.write("filename,status,timestamp\n")

    with open(os.path.join(os.getcwd(), "log.csv"), "a+") as file:
        file.write(data + "\n")

    return True


def format_data(log):
    """Converts and returns dict data to comma seperated string to save to csv

    @params log: dict of log
    """
    data = str(",".join([log["name"], log["okay"], log["timestamp"]]))
    return data


def testFile(filename, test_value):
    """Test the file against test_value

    @params filename: filename to be tested
    @params test_value: vaue to be checked against
    """
    filepath = os.path.join(ROOT_DIR, filename)
    log = {"name": "", "okay": "", "timestamp": ""}  # initialise dict

    command = "ipy {}.py {}".format(filepath, test_value)
    value = subprocess.check_output(command, shell=True).rstrip()
    timestamp = datetime.datetime.utcnow().isoformat()

    log["name"] = filename
    log["timestamp"] = timestamp
    log["okay"] = value.decode("utf8")

    data = format_data(log)
    write_log(data)
    print(log)


if __name__ == "__main__":
    testFile("checkOdd", 7)
    testFile("palindrome", "Malayalam")
