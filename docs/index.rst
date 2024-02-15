Documentation Demo
==================

This is a demo page to show how to use Readthedocs to automatically generate documentation website based on your **python** code. Other code such as *Arduino*, *C++* should also be supported but needs to be tested.

Readthedocs automatically pulls docstring from your code file. Some useful tutorials can be found `here <https://docs.readthedocs.io/en/stable/tutorial/index.html>`_, `here <https://pythonforthelab.com/blog/documenting-with-sphinx-and-readthedocs/>`_, and `here <https://amazonwebshark.com/open-source-documentation-with-read-the-docs/>`_.

Different from GitHub, Readthedocs uses reStructuredText (``.rst`` format, instead of ``.md`` format of Markdown) for plain text markup. Here are some cheat sheets of the ``.rst`` format:

* https://docs.anaconda.com/restructuredtext/index.html
* https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst
* https://sphinx-tutorial.readthedocs.io/cheatsheet/

This demonstrates the page reference function: :doc:`factorial` and :doc:`people`. 

Setup
-----

#. Register an account on https://readthedocs.org/. In the ``Settings`` page, connect your GitHub account.

   .. image:: /img/readthedocs_setting_page.png
      :align: center

#. Fork this repo (https://github.com/biomechatronics001/ReadTheDocs_PythonTest) and name the new repo based on your project. You will use it as a starting point.

#. Go back to your Readthedocs homepage, click the ``Import a Project`` button on the top of the page, and then select the repository you just created by clicking the **+** sign next to it. 

   .. image:: /img/readthedocs_import_project_page.png
      :align: center
   
   .. image:: /img/readthedocs_import_repository_page.png
      :align: center

   .. caution::
      Please make sure that the repository you created is set to **public** in order for Readthedocs to access it.

#. Readthedocs will import the selected repository and starting building the website. Under the ``Builds`` tab, you can see the build progress or errors. Typically the build should finish in about 30 seconds. Once the build passes, press the green ``View Docs`` button on the top right corner of the page. It will open up a webpage which is the same as the page you are looking at right now.

   .. image:: /img/readthedocs_first_success_homepage.png
      :align: center

#. Now your webpage is live online and you could copy the url and share it with others! By default, Readthedocs tracks the repository such that each ``push`` operation will trigger a rebuild (update) of the entire webpage, as you can see in the ``Builds`` tab. 

Visual Studio Code Setup (Optional but Highly Recommended)
----------------------------------------------------------

#. As mentioned above, each ``push`` operation to the repository will automatically trigger a rebuild of the webpage. Although this process is relatively fast (\< 1 min), it is still preferrable if we can see the changes reflected *locally* and *in real time* before pushing the changes to GitHub. In this case, we can use Visual Studio Code (VSCode) by Microsoft. VSCode can be downloaded from here: https://code.visualstudio.com/download.

#. Clone the GitHub repository you just created to your local PC and open the folder in VSCode through ``File -> Open Folder`` menu.

#. Open the ``conf.py`` file under ``docs`` folder. Select the Python interpreter by pressing ``Ctrl+Shift+P`` and type ``python select interpreter`` in the popup window. Click ``>python: Select interpreter`` and choose the python execuble you want to use. According to `this page <https://docs.restructuredtext.net/articles/prerequisites>`_, you can also select a virtual python environment.

#. Install ``sphinx 7.1.2`` and ``sphinx-book-theme 1.1.1`` into your selected python environment by executing ``/path/to/your/python/executable -m pip install sphinx==7.1.2 sphinx-book-theme==1.1.1``. If you are using a virtual environment, activate it first and then execute ``conda install sphinx==7.1.2 sphinx-book-theme==1.1.1``. Sphinx is the rendering engine.

#. Go to the ``Extensions`` tab on the left panel of VSCode. Install the ``Python`` extension by Microsoft and any subsequent extensions it prompts you to install. Then install ``Live Preview`` extension by Microsoft. Then install ``reStructuredText`` extension from LeXtudio Inc. Then install ``reStructuredText Syntax Highlighting`` extension from Trond Snekvik if VSCode doesn't automatically prompt you to do so. In the end, VSCode should also prompt you to install ``esbonio``, please also install it.

   .. image:: /img/vscode_restructuredtext_plugins.png
      :align: center
      :width: 250

#. Now you should see a ``esbonio`` label on the bottom status bar of VSCode. If you click it, it will probably says ``esbonio: Sphinx build error``. Don't worry. Open the ``settings.json`` file under ``.vscode`` folder that was just created. Add the following lines and save the file:

   .. code-block:: json

      {
         "esbonio.sphinx.confDir": "${workspaceFolder}/docs"
      }

#. Click the ``esbonio`` label on the bottom status bar again to rebuild the webpage. If the build succeeds, you should see something like below.

   .. image:: /img/vscode_esbonio_status_bar.png
      :align: center

#. Now you should see a ``_build`` folder created under ``docs`` folder. Open the ``index.html`` under ``html`` subfolder in VSCode, and click the ``Preview`` button on the top right corner.

   .. image:: /img/vscode_show_html_preview.png
      :align: center

#. A webpage should automatically pop up in VSCode that looks like the following. Now each time you make some changes to any of the pages and save, the webpage on the right will automatically refresh to reflect the changes.

   .. image:: /img/vscode_code_with_html_preview.png
      :align: center

#. Now we will move to the next section and show how to modify this demo page based on your own project.

Modify the Contents
-------------------

#. The main configuration files are ``.readthedocs.yaml`` and ``/docs/conf.py``. You could infer the meaning of each settings by their names. Please keep most of the settings unchanged unless **you understand what you are doing**. However, you should change the ``project``, ``copyright``, ``author``, ``release``, and ``version`` information in ``/docs/conf.py`` to fit your own identity.

#. The main page is ``/docs/index.rst``. Each other page should have their own ``.rst`` file and be added to the main page under ``.. toctree::``.

   .. note::

      Different from GitHub, Readthedocs uses reStructuredText (``.rst`` format, instead of ``.md`` format of Markdown) for plain text markup. Here are some cheat sheets of the ``.rst`` format:

      * https://docs.anaconda.com/restructuredtext/index.html
      * https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst
      * https://sphinx-tutorial.readthedocs.io/cheatsheet/
  
   .. note::

      Sphinx requires that the toctree lists include all pages. If a page is not in any toctree list, it is a page with no parent page, or an “orphan” page, and the Sphinx build will produce an error. If for some reason a page must be in the documentation but not in the left navigation, the ``:orphan:`` directive can be added at the top of that page so that Sphinx will build without errors (as seen on this page!). Please avoid the ``:orphan:`` directive as much as possible.

#. In this demo, we showed two codes (``factorial.py`` and ``people.py``) used as Python modules, i.e., they are saved under ``my_module`` folder with a ``__init__.py`` file. Typically, each ``.py`` file should be accompanied with a corresponding ``.rst`` file under ``docs`` (or subfolder of ``docs``). They don't need to share the same name but it is recommended to do so. 

   .. note::

      You must put the python codes under a folder and have a ``__init__.py`` file to declare these codes as modules. However, the ``__init__.py`` file can be an empty file.

#. In ``my_module/factorial.py``, a function ``factorial()`` is defined. Similarily, in ``my_module/people.py``, two classes ``People`` and ``Teacher`` are defined, where ``Teacher`` subclasses ``People``. All the documentation should be put in the triple quotation marks as shown in the file. Doc test is also supported by using the ``>>>`` symbol.

   .. note::

      Check in the documentation of the class ``Teacher`` in ``my_module/people.py`` how we use the internal cross-reference ``:class:`Person``` to link to the documentation of its parent class ``People``.

Document cpp files
------------------

Available resources:

* https://devblogs.microsoft.com/cppblog/clear-functional-c-documentation-with-sphinx-breathe-doxygen-cmake/
* https://medium.com/@aytackahveci93/documenting-c-code-with-sphinx-d6315b338615
* https://medium.com/practical-codingc-documentation-with-doxygen-cmake-sphinx-breathe-for-those-of-use-who-are-totally-lost-7d555386fe13



.. note::

   This project is under active development as of 02/14/2024.
   
   Build ver: 12



Contents
--------

.. toctree::
    :caption: Contents:

    factorial
    people
    Foo
    Foo2
    cat