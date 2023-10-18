from ward import test
from ward._run import run

import package1

@test("hello() returns 'hello world!'")
def _():
    assert package1.hello() == "hello world!"


if __name__ == "__main__":
    run()
