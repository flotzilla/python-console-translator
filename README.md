Python 3 console translator
-----
Translate text from english language to russian and backwards using Yandex translator. The language will be detected automatically.

If you wanna use quote char, add \ argument before quote char, like `\'`, but translator understand words without quote char.  

Add execution permissions for script with
 `chmod +x yndxt.py`

And run with `python3 yndxt.py your sentence for translating`

**You can add alias for bash**

In your `.bashrc` file add line like

`alias ytr="python3 /home/user_name/yndxt/yndxt.py`

and than run

`source .bashrc`

Now run script with `ytr your sentence for translating`

Also, save translation result to `/home/user_name/ytr-words.txt` file
