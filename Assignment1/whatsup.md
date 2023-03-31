# Mocking
Mocking, in the context of software development and testing, is a technique where a programmer creates a fake or simulated version of a dependency (such as a module, object, or function) to mimic its behavior. This allows developers to isolate the code they are testing from external factors and focus on the functionality of the specific component being tested.

The primary purpose of mocking is to enable unit testing, which is testing individual components of a system in isolation. Mocks can help developers achieve this by replacing complex or hard-to-reproduce dependencies with simpler, controllable substitutes that can be easily manipulated for various test scenarios.

# Functions
```assert_called_once_with(*args, **kwargs)``` asserts  that the mock was called **exacly** once and that call was with the specific argument.

```MagicMock``` allows you to mock an object easily. For instance if we have a sensor that takes 10 seconds to give an answer, we may use the MagicMock to give it a default returnvalue, so that we do not need to wait 10 seconds every time. This makes the unit test faster and basically better since we really do not care about the functionality of the sensor, we are only interested in the returnvalue. To import it: ```from unittest.mock import MagicMock```

MagicMock allows for other methods, one of those being ```assert_called_once``` that checks so that the method used is called **once**

So to sum the life of a mock:
- Create an instance of a class we want to mock
- Set mock expectations(eg return value)
- Invoke SUT(Software under test, i.e the unit we are currently testing)
- Validate expectations

Before writing your mocks, please keep in mind that:
- Mock stable dependencies
- Mock local dependencies
- Mock only one layer of dependencies


# Docs
Unittest - https://docs.python.org/3/library/unittest.mock.html