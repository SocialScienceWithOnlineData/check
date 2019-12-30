### Boilerplate
from IPython.core.display import display, HTML

### answers object.  Each q has a code (key) and a correct answer (value).
answers = {}
# Arithmetic
answers['try_it_out'] = 8
answers['leading_zero'] = {'correct':1,'minmul':1,'maxmul':3}
answers['big_numbers'] = 50000000000
answers['arithmetic1'] = 3*4+5+6
answers['arithmetic2'] = {'correct':(4*5)-(4-3),(4*5)-4-3:'Did you forget parentheses?'}
answers['spaces_in_arithmetic1'] = {'correct':4,'minmul':1,'maxmul':4}
answers['spaces_in_arithmetic2'] = {'correct':3,'minmul':1,'maxmul':4}
answers['parentheses'] = {'correct':1,'minmul':1,'maxmul':2}
# Modules
answers['import_syntax1'] = {'correct':2,'minmul':1,'maxmul':3}
answers['import_syntax2'] = {'correct':2,'minmul':1,'maxmul':3}
answers['scientific_notation'] = {'correct':3,'minmul':1,'maxmul':5}
# Output
answers['code_blocks_output1'] = {'correct':3,'minmul':1,'maxmul':7}
answers['code_blocks_output2'] = {'correct':3,'minmul':1,'maxmul':7}
answers['code_blocks_output3'] = {'correct':7,'minmul':1,'maxmul':7}
answers['code_blocks_output4'] = {'correct':5,'minmul':1,'maxmul':7}
answers['code_blocks_output5'] = {'correct':5,'minmul':1,'maxmul':7}
# Variables
answers['variable_names1'] = {'correct':1,'minmul':1,'maxmul':2}
answers['variable_names2'] = {'correct':1,'minmul':1,'maxmul':2}
answers['variable_names3'] = {'correct':2,'minmul':1,'maxmul':2}
answers['variable_names4'] = {'correct':1,'minmul':1,'maxmul':2}
answers['variable_names5'] = {'correct':1,'minmul':1,'maxmul':2}
answers['variable_names6'] = {'correct':1,'minmul':1,'maxmul':2}
answers['variable_names7'] = {'correct':2,'minmul':1,'maxmul':2}
answers['variable_names_cont1'] = {'correct':2,'minmul':1,'maxmul':3}
answers['variable_names_cont2'] = {'correct':3,'minmul':1,'maxmul':3}
answers['variable_assignment1'] = {'correct':5,'minmul':1,'maxmul':5}
answers['variable_assignment2'] = {'correct':3,'minmul':1,'maxmul':5}
answers['variable_assignment3'] = {'correct':2,'minmul':1,'maxmul':5}
answers['variable_name_quality1'] = {'correct':3,'minmul':1,'maxmul':4}
answers['reassignment1'] = {'correct':1,'minmul':1,'maxmul':3,'listans':[5,55,555]}
answers['reassignment2'] = {'correct':2,'minmul':1,'maxmul':3,'listans':[5,55,555]}
answers['reassignment3'] = {'correct':2,'minmul':1,'maxmul':3,'listans':[10,30]}
answers['reassignment4'] = {'correct':1,'minmul':1,'maxmul':3,'listans':[10,30]}
answers['reassignment5'] = 9
answers['reassignment6'] = 5
answers['reassignment7'] = 7



###  styling of user feedback
stylehtml =  """
<style>
  h1 {    
    display:inline-block;
    padding: 10px;
  }
  h1.right {    
    background-color: #dff0d8;    
    border-color: #d0e9c6;    
    color: #3c763d;    
  }
  h1.wrong {    
    background-color: #fcf8e3;    
    border-color: #faf2cc;    
    color: #8a6d3b; 
  }
  h1.error {    
    background-color: #fcf8e3;    
    border-color: #faf2cc;    
    color: #8a6d3b; 
  }
  h2.wrong {    
    background-color: #fcf8e3;    
    border-color: #faf2cc;    
    color: #8a6d3b; 
  }
</style>
"""
correct = HTML( stylehtml + '<h1 class="right">Correct!</h1>')
incorrect = HTML( stylehtml + '<h1 class="wrong">Try again.</h1>')
def broken_key(key):
  return HTML(stylehtml + '<h1 class="error">check(\'{}\',...) error name \'{}\' was modified!</h1>'.format(key,key))

def incorrect_with_hint(hint):
  return HTML(stylehtml + '<h1 class="wrong">Try again.</h1>\n<h2 class="wrong">Hint: {}</h2>'.format(hint))

def check(key, answer):
  if answer == ...:
    return
  if key not in answers:
    display(broken_key(key))
    return
  test = answer == answers[key]
  if test:
    display( correct )
  elif not isinstance(answers[key],dict):
    display( incorrect )
  else:
    test = answer == answers[key]['correct']
    if test:
      display( correct )
    elif 'minmul' in answers[key]:
      if not isinstance(answer,int) or int(answer) < answers[key]['minmul'] or int(answer) > answers[key]['maxmul']:
        if 'listans' in answers[key] and answer in answers[key]['listans']:
          display(incorrect_with_hint('Make sure to select the multiple choice number, not associated answer.'))
        else:
          display(incorrect_with_hint('Select the multiple choice number between {} and {}.'.format(answers[key]['minmul'],answers[key]['maxmul'])))
    elif 'attempts' in answers[key]:
      if answer in answers[key]:
        display(incorrect_with_hint(answers[key][answer]))
      elif answers[key] > 3 and 'hint' in answers[key]:
        display(incorrect_with_hint(answers[key]['hint']))
      else:
        display( incorrect )
      answers[key]['attempts'] += 1
    else:
      display( incorrect )
      answers[key]['attempts'] = 1  
  return( test )
