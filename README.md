# Fake Agent
Generate fake user agents on the fly


# Features
- Works offline
- Easy to use


# Usage
**Import and initialize the `Fake_Agent` class**
```python
from FakeAgent import Fake_Agent

fa = Fake_Agent()
```

- `get()` - Get user agents as a list or generator according to the browser that Fake_Agent class initialized with
    - For more info, run,
        ```python
        >>> print(help(fa.get))

        >>>
        Help on method get in module FakeAgent.faker:

        get(as_gen: bool = False) method of FakeAgent.faker.Fake_Agent instance
        
        Get user agents as a list or generator according to given browser
    
        ### Arguments
    
            - `as_gen` :bool (optional) - Pass "True" if you want to return value as a generator rather than a list
        ```
    - Example:
        ```python
        fa.get()
        ```

- `random()` - Randomly select user agent
    - For more info, run,
        ```python
        >>> print(help(fa.random))

        >>>
        Help on method random in module FakeAgent.faker:

        random(mix_browsers: bool = False, with_details: bool = False) method of FakeAgent.faker.Fake_Agent instance

        Randomly select user agent
    
        ### Arguments
    
            - `mix_browsers` :bool (optional) - Pass "True" if you want to randomly select browser too
            - `with_details` :bool (optional) - Pass "True" if you need to get browser
        ```
    - Example:
        ```python
        fa.random(with_details=True)
        ```


# License
Licensed under [MIT License](LICENSE)