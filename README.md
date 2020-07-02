# check
Interactive low-stakes local micro-assessments for notebook based Python pedagogy, for UC Davis CMN152V

# INSTALL
```
%pip install --user --upgrade git+https://github.com/SocialScienceWithOnlineData/check.git
from check import check
```
# USE
```
# <add to check/__init__.py a question/answer pair with q label `a_question`>
check('a_question', ...) # seed this under question `a_question`
# <instruct student to fill in `...` with the right answer.
```
