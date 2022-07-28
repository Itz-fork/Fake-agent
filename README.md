# Fake Agent
Generate fake user agents on the fly


# Features
- Easy to use
- Works offline
- No need of 3rd party packages


# Install

- Via pip
    ```
    pip3 install fake-agent
    ```
- Via source
    ```
    pip3 install git+https://github.com/Itz-fork/Fake-agent.git
    ```


# Usage
For more detailed explanation, visit [documentation on usage](https://itz-fork.github.io/Fake-agent/#/usage)


**Import and initialize the `Fake_Agent` class**

```python
from FakeAgent import Fake_Agent

fa = Fake_Agent()
```


- `get()` - Get user agents as a list or generator according to the browser that Fake_Agent class initialized with
    - For more info visit - [Fake_Agent.get documentation](https://itz-fork.github.io/Fake-agent/#/get)

- `random()` - Randomly select user agent
    - For more info visit - [Fake_Agent.random documentation](https://itz-fork.github.io/Fake-agent/#/random)


# License
Licensed under [MIT License](LICENSE)