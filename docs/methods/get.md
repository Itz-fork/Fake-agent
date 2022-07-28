# Get user agents
Get user agents as a list or generator according to the browser that `Fake_Agent` class initialized with


## Arguments
- `browser` :Enum (optional) - Enum of the browser you want to get user agents. Defaults to the browser that Fake_Agent class initialized with
- `as_gen` :bool (optional) - Return value as a generator rather than a list. Defaults to `False`


## Examples
- Get user agents of current browser
    ```python
    from FakeAgent import Fake_Agent
    
    fa = Fake_Agent()
    print(fa.get())
    ```

- Get user agents of a differant supported browser. In this case chrome
    ```python
    from FakeAgent import Fake_Agent
    from FakeAgent.types import Browsers
    
    fa = Fake_Agent()
    print(fa.get(browser=Browsers.CHROME))
    ```