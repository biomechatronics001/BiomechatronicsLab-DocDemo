Documentation Demo
==================

This is a demo page to show how to use Readthedocs to automatically generate documentation website based on your **python** code. Other code such as *Arduino*, *C++* should also be supported but needs to be tested.

Readthedocs automatically pulls docstring from your code file. Some useful tutorials can be found `here <https://docs.readthedocs.io/en/stable/tutorial/index.html>`_, `here <https://pythonforthelab.com/blog/documenting-with-sphinx-and-readthedocs/>`_, and `here <https://amazonwebshark.com/open-source-documentation-with-read-the-docs/>`_.

Different from GitHub, Readthedocs uses reStructuredText (``.rst`` format, instead of ``.md`` format of Markdown) for plain text markup. Here are some cheat sheets of the ``.rst`` format are as below:

* https://docs.anaconda.com/restructuredtext/index.html
* https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst
* https://sphinx-tutorial.readthedocs.io/cheatsheet/

This demonstrates the page reference function: :doc:`factorial` and :doc:`people`. 

Setup
-----

#. Register an account on https://readthedocs.org/. In the ``Settings`` page, connect your GitHub account.

   .. image:: /img/readthedocs_setting_page.png
      :align: left

#. Fork this repo (https://github.com/biomechatronics001/ReadTheDocs_PythonTest) and name the new repo based on your project. You will use it as a starting point.

#. Go back to your Readthedocs homepage, click the ``Import a Project`` button on the top of the page, and then select the repository you just created by clicking the **+** sign next to it. 

   .. image:: /img/readthedocs_import_project_page.png
      :align: left
   
   .. image:: /img/readthedocs_import_repository_page.png
      :align: left

   .. caution::
      Please make sure that the repository you created is set to **public** in order for Readthedocs to access it.

#. Readthedocs will import the selected repository and starting building the website. Under the ``Builds`` tab, you can see the build progress or errors. Typically the build should finish in about 30 seconds. Once the build passes, press the green ``View Docs`` button on the top right corner of the page. It will open up a webpage which is the same as the page you are looking at right now.

   .. image:: /img/readthedocs_first_success_homepage.png
      :align: left

#. Now your webpage is live online and you could copy the url and share it with others! By default, Readthedocs tracks the repository such that each ``push`` operation will trigger a rebuild (update) of the entire webpage, as you can see in the ``Builds`` tab. 

Visual Studio Code Setup (Optional but Highly Recommended)
----------------------------------------------------------

#. As mentioned above, each ``push`` operation to the repository will automatically trigger a rebuild of the webpage. Although this process is relatively fast (\< 1 min), it is still preferrable if we can see the changes reflected *locally* and *in real time* before pushing the changes to GitHub. In this case, we can use Visual Studio Code (VSCode) by Microsoft. VSCode can be downloaded from here: https://code.visualstudio.com/download.

#. Clone the GitHub repository you just created to your local PC and open the folder in VSCode through ``File -> Open Folder`` menu.

#. Next we will show how to modify this demo page.

Modify the Contents
-------------------

#. 



.. note::

   This project is under active development as of 02/13/2024.
   
   Build ver: 8

Contents
--------

.. toctree::
    :caption: Contents:

    factorial
    people