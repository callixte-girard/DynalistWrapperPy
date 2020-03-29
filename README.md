# Purpose

Access the Dynalist API easily thanks to this unofficial Python Dynalist wrapper : https://pypi.org/project/dynalist/
But contrary to it (which is almost docless), this little code gives you a template just ready to start.

# Setup

- Install Dynalist via `pip` (Python package manager) : `pip install dynalist`
    - You may use `pip3` instead of `pip`.
    - You should (imho) use a `virtualenv` to install your packages for this project, but that will work with both methods.
- Get a `token` via Dynalist site on this page —> https://dynalist.io/developer
- Replace it in `static/constants.py`, in the variable `dynalist_token`.
- Specify the id of the page you want to get in `your_file_id`.
    - You can use the screenshot I provided to help you.
        - To open the panel you can do `Cmd + Shift + I` (I'm on macOS, should probably replace `Cmd` with `Ctrl` on Windows)
        - You must click on the request `load` and find the value you need.
        - The sequence you need is circled in red.
    - Here is another (simpler) method :
        - Go to Dynalist in your web browser and go to the page you want to get the id.
        - Simply copy the last part of the URL (like in the screenshot).
- Launch the file `main.py` with Python : `python main.py` (here you may as well use `python3` instead of `python`.)
- It should give you some JSON containing the document whose id you passed it. If it is the case, congrats, it's working ;)