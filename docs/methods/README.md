# Fake agent class
This is main class of the Fake agent library.


## Initialize
You can initialize Fake agent by importing it as follows,
```python
from FakeAgent import Fake_Agent

fa = Fake_Agent()
```


## Arguments
`Fake_Agent` class accepts following keyword arguments,

- `browser` :Enum (optional) - Enum of the browser that you want to use (check [enums]() for more info)
- `load_on_init` :bool (optional) - Whether you want to load json file to memory on initialization


## Methods
`Fake_Agent` class consist of following methods

- [`get`](./get.md)
- [`random`](./random.md)
- [`browser specific methods`](./browser_methods.md)