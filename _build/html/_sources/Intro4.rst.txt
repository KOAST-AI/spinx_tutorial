============================
4. 소스 설명 예제
============================


4. **소스 설명**
----------------------------
::

    def func(arg1, arg2) :
        """Summary line.

        Extended description of function.

        Args:
            arg1: 1번 독립 변수 설명
            arg2: 2번 독립변수 설명

        Returns:
            리턴해줄 값

        """
        return True

def func(arg1, arg2) :
        """Summary line.

        Extended description of function.

        Args:
            arg1: 1번 독립 변수 설명
            arg2: 2번 독립변수 설명

        Returns:
            리턴해줄 값

        """
        return True


프로젝트 정보 출력
------------------------
::

        ## Sphinx 문법 사용
        .. literalinclude:: ./conf.py
        :language: python
        :linenos:
        :emphasize-lines: 3
        :lines: 20-25


사용 결과
""""""""""""""""""""""""""""""""""

.. literalinclude:: ./conf.py
   :language: python
   :linenos:
   :emphasize-lines: 3
   :lines: 20-25





예제 소스 출력
------------------------

.. literalinclude:: ./source.py
   :language: python
   :linenos:
   :emphasize-lines: 4,7
   :lines: 1-33
