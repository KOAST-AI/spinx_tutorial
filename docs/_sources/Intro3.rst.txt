============================
3. 문서 작성하기.
============================


3.1 Sphinx 디렉토리 기본구조
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

        doc
        ├─ _build
        │   ├─doctrees
        │   ├─html
        ├─ _static
        ├─ _templates
        ├─ conf.py
        ├─ index.rst
        ├─ make.bat
        └──Makefile

3.2 새로운 문서 페이지 추가.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


doc 하위 디렉토리에 Intor1.rst 파일 생성
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::

        ## title 작성 필수. title 없으면 에러 발생.

        1. 타이틀 작성 !!!!!
        ---------------------------


index.rst 파일 수정
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::

        .. test3 documentation master file, created by
        sphinx-quickstart on Mon Nov 30 17:21:10 2020.
        You can adapt this file completely to your liking, but it should at least
        contain the root `toctree` directive.

        Welcome to test3's documentation!
        =================================

        .. toctree::
        :maxdepth: 2
        :caption: Contents:

        ##################### Intor1 추가.#######################
        Intro1

        Indices and tables
        ==================

        * :ref:`genindex`
        * :ref:`modindex`
        * :ref:`search`

기존 빌드 지우기
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::  

        ## _build 하위 디렉토리 삭제됨.
        $ make clean 


Html 새로 생성
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::  

        ## 새로 적용된 html 파일 생성.
        $ make html


3.3 .py 소스코드 추가하기.(기존 작성 파일을 사용해도됨.)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


index.rst 파일 수정
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
::

        .. test3 documentation master file, created by
        sphinx-quickstart on Mon Nov 30 17:21:10 2020.
        You can adapt this file completely to your liking, but it should at least
        contain the root `toctree` directive.

        Welcome to test3's documentation!
        =================================

        .. toctree::
        :maxdepth: 2
        :caption: Contents:

        Intro1
        
        ## my_package 추가 ( my_package.rst 새로운 인덱스 페이지)
        my_package
        

        Indices and tables
        ==================

        * :ref:`genindex`
        * :ref:`modindex`
        * :ref:`search`


my_package.rst 파일 생성
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
doc 하위 디렉토리에 Intor1.rst 파일 생성 (index.rst 와 같은 레벨)


my_package.rst 파일에 아래 내용과 같이 작성.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
::

        my_package
        ======================================

        .. automodule:: my_package
        :members:
        :undoc-members:
        :show-inheritance:

        ## title Name

        Title Name
        -------------

        ## my_package 폴더에  my_module 사용  automodule 로 .py 를 html 로 쉽게 변경.
        .. automodule:: my_package.my_module
            :members:


my_package 폴더 생성
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::

        doc  하위 디렉토리에 my_packge 폴더 생성


my_module.py 생성.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::

        my_package  하위 디렉토리에 my_module.py 파일 생성


my_module.py 쓰기. 아래와 같이 작성하고 저장.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::

        들여쓰기
            들여쓰기와 
        """
        주석을 사용하여 소스코드를 문서화 하도록 도와줌.
        """


::

        """
            My Module
            ~~~~~~~~~~~~~~
        """

        class Test(object):
            """두 개의 int 값을 입력받아 다양한 연산을 할 수 있도록 하는 클래스.

            :param int a: a 값
            :param int b: b 값
            """

            def __init__(self, a, b):
                self._a = a
                self._b = b

            def is_same(self):
                """미리 입력받은 a와 b값이 같은지 확인하여 결과를 반환합니다.

                :return: boolean True or False에 대한 결과, a와 b가 값으면 True, 다르면 False

                예제:
                    다음과 같이 사용하세요:

                    >>> Test(1, 2).is_same()
                    False

                """
                return self._a == self._b

            def plus(self):
                """미리 입력받은 a와 b값을 더한 결과를 반환합니다.

                :returns: int a + b에 대한 결과

                예제:
                    다음과 같이 사용하세요:

                    >>> Test(2, 1).plus()
                    3


                """
                return self._a + self._b

빌드 지우고 html 재 생성
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::      

        $ make clean
        $ make html




error 발생시!
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
::

        !!error 발생시

        conf.py 파일 수정


        # extensions = []    아래와 같이 수정.
        extensions = ['sphinx.ext.autodoc']


정상 실행시 좌측 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
5. 패키지 소스 설명과 같은 페이지 생성~!!
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""





                
                


