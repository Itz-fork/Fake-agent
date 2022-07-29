# Fake Agent
```python
from FakeAgent import Fake_Agent

fa = Fake_Agent()
print(fa.random())
```

**Fake-agent**, generate fake browser user agents without a hassle!


## Links 🔗
- [Documentation 📔](https://itz-fork.github.io/Fake-agent)
- [Features 💪](#features-)
- [Installation ⬇️](#install-)
- [Usage 🤔](#usage-)
- [License 👮](#license-)


## Features 💪
- Easy to use
- Works offline
- No need to install bunch of 3rd party packages


## Install ⬇️
- Stable from [pypi](https://pypi.org/project/fake-agent)
    ```
    pip3 install fake-agent
    ```
- Bleeding edge from [github](https://github.com/Itz-fork/Fake-agent)
    ```
    pip3 install -U https://github.com/Itz-fork/Fake-agent/archive/master.zip
    ```


## Usage 🤔
For more methods and detailed explanation, visit [method documentation](https://itz-fork.github.io/Fake-agent/#/methods/README)


**Import and initialize the `Fake_Agent` class**

```python
from FakeAgent import Fake_Agent

fa = Fake_Agent()
```

- `get()` - Get user agents as a list or generator according to the browser that Fake_Agent class initialized with
    - For more info visit - [Fake_Agent.get documentation](https://itz-fork.github.io/Fake-agent/#/methods/get)

- `random()` - Randomly select user agent
    - For more info visit - [Fake_Agent.random documentation](https://itz-fork.github.io/Fake-agent/#/methods/random)


## License 👮
Licensed under [MIT License](LICENSE)