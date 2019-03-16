1. Create virtualenv:
    ````bash
    pip install virtualenv
    virtualenv env
    ```

2. enter virtualenv:
    ```bash
    # in linux or mac:
    source env/bin/activate
    # in windows:
    env/Scripts/activate.bat
    ```
3. install `pyserial`
   ```bash
    pip install pyserial
   ```

4. install `dash`
   ```bash
    pip install dash==0.39.0  # The core dash backend
    pip install dash-html-components==0.14.0  # HTML components
    pip install dash-core-components==0.44.0  # Supercharged components
    pip install dash-table==3.6.0  # Interactive DataTable component (new!)
    pip install dash-daq==0.1.0  # DAQ components (newly open-sourced!)
   ```
