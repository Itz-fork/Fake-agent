# Random user agent
Randomly select user agent


### Arguments
- `mix_browsers` :bool (optional) - To randomly select a browser. Defaults to `True`
- `with_details` :bool (optional) - To get user agent details (INTERNET REQUIRED). Defaults to `False`


### Examples
- Select random user agent of current browser with it's details
    ```python
    from FakeAgent import Fake_Agent
    
    fa = Fake_Agent()
    print(fa.random(with_details=True))
    ```

- Select user agent of a different supported browser. In this case chrome
    ```python
    from FakeAgent import Fake_Agent
    from FakeAgent.types import Browsers
    
    fa = Fake_Agent(Browsers.CHROME)
    print(fa.random(with_details=True))
    ```