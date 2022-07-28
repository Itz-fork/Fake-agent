# Get user agents
Get user agents as a list or generator according to the browser that Fake_Agent class initialized with


### Arguments
- `browser` :Enum (optional) - Pass Browser enum if you want to get user agents of a specific browser rather than the one you initialized the Fake_Agent class with
- `with_details` :bool (optional) - Pass `True` if you want to get the user agent's info too

### Examples

- Get user agents of current browser
    ```python
    from FakeAgent import Fake_Agent
    
    fa = Fake_Agent()
    print(fa.random(with_details=True))
    ```

- Get user agents of a differant supported browser. In this case chrome
    ```python
    from FakeAgent import Fake_Agent
    from FakeAgent.types import Browsers
    
    fa = Fake_Agent(Browsers.CHROME)
    print(fa.random(with_details=True))
    ```