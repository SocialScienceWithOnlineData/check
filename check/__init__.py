### Boilerplate
from IPython.core.display import display, HTML
# def  display(x):
#     pass
# def  HTML(x):
#     print(x)

### answers object.  Each q has a code (key) and a correct answer (value).
answers = {}
# Arithmetic
answers['try_it_out'] = {'l':2, 'correct':8}
answers['leading_zero'] = {'l':2, 'correct':1,'minmul':1,'maxmul':3}
answers['big_numbers'] = {'l':2, 'correct':50000000000}
answers['arithmetic1'] = {'l':2, 'correct':3*4+5+6}
answers['arithmetic2'] = {'l':2, 'correct':(4*5)-(4-3),(4*5)-4-3:'Did you forget parentheses?'}
answers['spaces_in_arithmetic1'] = {'l':2, 'correct':4,'minmul':1,'maxmul':4}
answers['spaces_in_arithmetic2'] = {'l':2, 'correct':3,'minmul':1,'maxmul':4}
answers['parentheses'] = {'l':2, 'correct':1,'minmul':1,'maxmul':2}
# Modules
answers['notebook_blocks'] = {'l':2, 'correct':1,'minmul':1,'maxmul':4}
answers['import_syntax1'] = {'l':2, 'correct':2,'minmul':1,'maxmul':3}
answers['import_syntax2'] = {'l':2, 'correct':2,'minmul':1,'maxmul':3}
answers['scientific_notation'] = {'l':2, 'correct':3,'minmul':1,'maxmul':5}
# Output
answers['code_blocks_output1'] = {'l':2, 'correct':3,'minmul':1,'maxmul':7}
answers['code_blocks_output2'] = {'l':2, 'correct':3,'minmul':1,'maxmul':7}
answers['code_blocks_output3'] = {'l':2, 'correct':7,'minmul':1,'maxmul':7}
answers['code_blocks_output4'] = {'l':2, 'correct':5,'minmul':1,'maxmul':7}
answers['code_blocks_output5'] = {'l':2, 'correct':5,'minmul':1,'maxmul':7}
# Variables
answers['variable_names1'] = {'l':2, 'correct':1,'minmul':1,'maxmul':2}
answers['variable_names2'] = {'l':2, 'correct':1,'minmul':1,'maxmul':2}
answers['variable_names3'] = {'l':2, 'correct':2,'minmul':1,'maxmul':2}
answers['variable_names4'] = {'l':2, 'correct':1,'minmul':1,'maxmul':2}
answers['variable_names5'] = {'l':2, 'correct':1,'minmul':1,'maxmul':2}
answers['variable_names6'] = {'l':2, 'correct':1,'minmul':1,'maxmul':2}
answers['variable_names7'] = {'l':2, 'correct':2,'minmul':1,'maxmul':2}
answers['variable_names_cont1'] = {'l':2, 'correct':2,'minmul':1,'maxmul':3}
answers['variable_names_cont2'] = {'l':2, 'correct':3,'minmul':1,'maxmul':3}
answers['variable_assignment1'] = {'l':2, 'correct':5,'minmul':1,'maxmul':5}
answers['variable_assignment2'] = {'l':2, 'correct':3,'minmul':1,'maxmul':5}
answers['variable_assignment3'] = {'l':2, 'correct':2,'minmul':1,'maxmul':5}
answers['variable_name_quality1'] = {'l':2, 'correct':3,'minmul':1,'maxmul':4}
answers['reassignment1'] = {'l':2, 'correct':1,'minmul':1,'maxmul':3,'listans':[5,55,555]}
answers['reassignment2'] = {'l':2, 'correct':2,'minmul':1,'maxmul':3,'listans':[5,55,555]}
answers['reassignment3'] = {'l':2, 'correct':2,'minmul':1,'maxmul':3,'listans':[10,30]}
answers['reassignment4'] = {'l':2, 'correct':1,'minmul':1,'maxmul':3,'listans':[10,30]}
answers['reassignment5'] = {'l':2, 'correct':9}
answers['reassignment6'] = {'l':2, 'correct':5}
answers['reassignment7'] = {'l':2, 'correct':7}

answers['errors1'] = {'l':3,'correct':4,'minmul':1,'maxmul':5}
answers['type1'] = {'l':3,'correct':4,'minmul':1,'maxmul':5}
answers['type2'] = {'l':3,'correct':4,'minmul':1,'maxmul':5}
answers['type3'] = {'l':3,'correct':1,'minmul':1,'maxmul':5}
answers['booleans1'] = {'l':3,'correct':2,'minmul':1,'maxmul':3}
answers['booleans2'] = {'l':3,'correct':4,'minmul':1,'maxmul':4}
answers['booleans3'] = {'l':3,'correct':1,'minmul':1,'maxmul':4}
answers['writing_strings1'] = {'l':3,'correct':'Hi Python'}
answers['writing_strings2'] = {'l':3,'correct':'abcdefghijklmnopqrstuvwxyz'}
answers['string_length1'] = {'l':3,'correct':3,'minmul':1,'maxmul':4}
answers['string_length2'] = {'l':3,'correct':7}
answers['string_length3'] = {'l':3,'correct':0}
answers['string_length4'] = {'l':3,'correct':4,'minmul':1,'maxmul':5}
answers['quote_types1'] = {'l':3,'correct':3,'minmul':1,'maxmul':5}
answers['substrings_in_strings1'] = {'l':3,'correct':4,'minmul':1,'maxmul':5}
answers['substrings_in_strings2'] = {'l':3,'correct':6,'minmul':1,'maxmul':6}
answers['combining_strings1'] = {'l':3,'correct':2,'minmul':1,'maxmul':5}
answers['combining_strings2'] = {'l':3,'correct':3,'minmul':1,'maxmul':4}
answers['comparing_things1'] = {'l':3,'correct':1,'minmul':1,'maxmul':2}
answers['comparing_things2'] = {'l':3,'correct':2,'minmul':1,'maxmul':2}
answers['comparing_things3'] = {'l':3,'correct':1,'minmul':1,'maxmul':2}
answers['comparing_things4'] = {'l':3,'correct':2,'minmul':1,'maxmul':2}
answers['comparing_things5'] = {'l':3,'correct':1,'minmul':1,'maxmul':2}
answers['comparing_things6'] = {'l':3,'correct':2,'minmul':1,'maxmul':2}
answers['comparing_things7'] = {'l':3,'correct':1,'minmul':1,'maxmul':2}
answers['comparing_things8'] = {'l':3,'correct':2,'minmul':1,'maxmul':2}
answers['comparing_things9'] = {'l':3,'correct':2,'minmul':1,'maxmul':2}
answers['comparing_things10'] = {'l':3,'correct':2,'minmul':1,'maxmul':2}
answers['comparing_things11'] = {'l':3,'correct':2,'minmul':1,'maxmul':2}
answers['comparing_things12'] = {'l':3,'correct':1,'minmul':1,'maxmul':2}
answers['comparing_things13'] = {'l':3,'correct':3,'minmul':1,'maxmul':4}
answers['comparing_things14'] = {'l':3,'correct':1,'minmul':1,'maxmul':2}
answers['compare_v_assign1'] = {'l':3,'correct':1,'minmul':1,'maxmul':3}
answers['compare_v_assign2'] = {'l':3,'correct':3,'minmul':1,'maxmul':5}
answers['relative_comparisons1'] = {'l':3,'correct':2,'minmul':1,'maxmul':4}
answers['relative_comparisons2'] = {'l':3,'correct':4,'minmul':1,'maxmul':4}

answers['list_definitions1'] = {'l':4,'correct':[1, 2, 3]}
answers['list_definitions2'] = {'l':4,'correct':["1", "2", "3"]} ## could also be [‘1’, ’2’, ’3’]
answers['list_definitions3'] = {'l':4,'correct':2,'minmul':1,'maxmul':7}
answers['list_type1'] = {'l':4,'correct':2,'minmul':1,'maxmul':3}
answers['list_indexing1'] = {'l':4,'correct': 5,'minmul':1,'maxmul':5}
answers['list_indexing2'] = {'l':4,'correct':3,'minmul':1,'maxmul':5}
answers['list_indexing3'] = {'l':4,'correct':0,'minmul':0,'maxmul':4}
answers['list_indexing4'] = {'l':4,'correct':1,'minmul':1,'maxmul':3}
answers['list_errors1'] = {'l':4,'correct':6,'minmul':1,'maxmul':6}
answers['list_slicing1'] = {'l':4,'correct':3,'minmul':1,'maxmul':4}
answers['list_slicing2'] = {'l':4,'correct':5,'minmul':1,'maxmul':5}
answers['list_slicing3'] = {'l':4,'correct':5,'minmul':1,'maxmul':5}
answers['list_slicing4'] = {'l':4,'correct':5,'minmul':1,'maxmul':7}
answers['list_slicing5'] = {'l':4,'correct':1,'minmul':1,'maxmul':3}
answers['list_slicing6'] = {'l':4,'correct':2,'minmul':1,'maxmul':3}
answers['list_slicing7'] = {'l':4,'correct':1,'minmul':1,'maxmul':3}
answers['list_changes1'] = {'l':4,'correct':5,'minmul':1,'maxmul':6}
answers['list_changes2'] = {'l':4,'correct':5,'minmul':1,'maxmul':6}
answers['list_edits1'] = {'l':4,'correct':2,'minmul':1,'maxmul':3}
answers['list_edits2'] = {'l':4,'correct':2,'minmul':1,'maxmul':3}
answers['list_edits3'] = {'l':4,'correct':2,'minmul':1,'maxmul':3}
answers['list_edits4'] = {'l':4,'correct':3,'minmul':1,'maxmul':3}
answers['list_edits5'] = {'l':4,'correct':3,'minmul':1,'maxmul':3}
answers['list_edits6'] = {'l':4,'correct':2,'minmul':1,'maxmul':3}
answers['list_edits7'] = {'l':4,'correct':1,'minmul':1,'maxmul':3}
answers['list_edits8'] = {'l':4,'correct':3,'minmul':1,'maxmul':3}
answers['list_edits9'] = {'l':4,'correct':1,'minmul':1,'maxmul':3}
answers['list_edits10'] = {'l':4,'correct':1,'minmul':1,'maxmul':3}
answers['list_edits11'] = {'l':4,'correct':2,'minmul':1,'maxmul':3}
answers['list_edits12'] = {'l':4,'correct':3,'minmul':1,'maxmul':3}
answers['growing_lists1'] = {'l':4,'correct':1,'minmul':1,'maxmul':2}
answers['growing_lists2'] = {'l':4,'correct':2,'minmul':1,'maxmul':2}
answers['growing_lists3'] = {'l':4,'correct':3,'minmul':1,'maxmul':4} ## check this one
answers['growing_lists4'] = {'l':4,'correct':3,'minmul':1,'maxmul':4}
answers['list_addition1'] = {'l':4,'correct':6,'minmul':1,'maxmul':6}
answers['list_addition2'] = {'l':4,'correct':4,'minmul':1,'maxmul':6}
answers['list_addition3'] = {'l':4,'correct':6,'minmul':1,'maxmul':6}
answers['empty_string1'] = {'l':4,'correct':5,'minmul':1,'maxmul':5}
answers['empty_string2'] = {'l':4,'correct':3,'minmul':1,'maxmul':4}
answers['empty_string3'] = {'l':4,'correct':2,'minmul':1,'maxmul':4}
answers['list_contents1'] = {'l':4,'correct':4,'minmul':1,'maxmul':6}
answers['list_contents2'] = {'l':4,'correct':4,'minmul':1,'maxmul':4}
answers['list_contents3'] = {'l':4,'correct':2,'minmul':1,'maxmul':4}
answers['list_contents4'] = {'l':4,'correct':1,'minmul':1,'maxmul':2}
answers['list_contents5'] = {'l':4,'correct':2,'minmul':1,'maxmul':2}
answers['list_contents6'] = {'l':4,'correct':2,'minmul':1,'maxmul':2}
answers['list_contents7'] = {'l':4,'correct':1,'minmul':1,'maxmul':2}
answers['list_contents8'] = {'l':4,'correct':2,'minmul':1,'maxmul':2}
answers['list_counts1'] = {'l':4,'correct':4,'minmul':1,'maxmul':7}
answers['list_counts2'] = {'l':4,'correct':2,'minmul':1,'maxmul':7}
answers['list_counts3'] = {'l':4,'correct':6,'minmul':1,'maxmul':7}
answers['list_counts4'] = {'l':4,'correct':2,'minmul':1,'maxmul':7}
answers['list_counts5'] = {'l':4,'correct':6,'minmul':1,'maxmul':7}
answers['list_summarizing1'] = {'l':4,'correct':3}
answers['list_summarizing2'] = {'l':4,'correct':18}
answers['list_summarizing3'] = {'l':4,'correct':2}
answers['list_summarizing4'] = {'l':4,'correct':1,'minmul':1,'maxmul':3}
answers['list_transforming1'] = {'l':4,'correct':1,'minmul':1,'maxmul':3}
answers['list_transforming2'] = {'l':4,'correct':2,'minmul':1,'maxmul':3}
answers['list_transforming3'] = {'l':4,'correct':2,'minmul':1,'maxmul':3}
answers['list_transforming4'] = {'l':4,'correct':3,'minmul':1,'maxmul':3}
answers['list_transforming5'] = {'l':4,'correct':3,'minmul':1,'maxmul':8}

answers['loop1'] = {'l':5,'correct':3 ,'minmul':1,'maxmul':5}
answers['loop2'] = {'l':5,'correct':6,'minmul':1,'maxmul':6}
answers['loop3'] = {'l':5,'correct':5,'minmul':1,'maxmul':8}
answers['loop4'] = {'l':5,'correct':4,'minmul':1,'maxmul':5}
answers['loop5'] = {'l':5,'correct':4,'minmul':1,'maxmul':4}
answers['loop6'] = {'l':5,'correct':3,'minmul':1,'maxmul':4}
answers['loop7'] = {'l':5,'correct':1,'minmul':1,'maxmul':5}
answers['replace1'] = {'l':5,'correct':3,'minmul':1,'maxmul':5}
answers['replace2'] = {'l':5,'correct':2,'minmul':1,'maxmul':4}
answers['replace3'] = {'l':5,'correct':1,'minmul':1,'maxmul':4}
answers['growdata1'] = {'l':5,'correct':4,'minmul':1,'maxmul':6}
answers['growdata2'] = {'l':5,'correct':5,'minmul':1,'maxmul':6}
answers['growdata3'] = {'l':5,'correct':4,'minmul':1,'maxmul':5}
answers['growdata4'] = {'l':5,'correct':2,'minmul':1,'maxmul':5}
answers['forloop1'] = {'l':5,'correct':5,'minmul':1,'maxmul':6}
answers['forloop2'] = {'l':5,'correct':5,'minmul':1,'maxmul':6}
answers['forloop3'] = {'l':5,'correct':5,'minmul':1,'maxmul':6}
answers['forloop4'] = {'l':5,'correct':4,'minmul':1,'maxmul':8}
answers['forloop5'] = {'l':5,'correct':1,'minmul':1,'maxmul':8}
answers['forloop6'] = {'l':5,'correct':1,'minmul':1,'maxmul':8}
answers['forloop7'] = {'l':5,'correct':3,'minmul':1,'maxmul':8}

#6
answers['loopcond1'] = {'l':6,'correct':3,'minmul':1,'maxmul':4}
answers['loopcond2'] = {'l':6,'correct':2,'minmul':1,'maxmul':4}
answers['loopcond3'] = {'l':6,'correct':1,'minmul':1,'maxmul':4}
answers['loopcond4'] = {'l':6,'correct':4,'minmul':1,'maxmul':7}
answers['loopcond5'] = {'l':6,'correct':1,'minmul':1,'maxmul':3}
answers['loopcond6'] = {'l':6,'correct':3,'minmul':1,'maxmul':5}
answers['loopcond7'] = {'l':6,'correct':4,'minmul':1,'maxmul':4}
answers['loopcond8'] = {'l':6,'correct':7,'minmul':1,'maxmul':7}
answers['iflong1'] = {'l':6,'correct':6,'minmul':1,'maxmul':7}
answers['iflong2'] = {'l':6,'correct':7,'minmul':1,'maxmul':7}
answers['iflong3'] = {'l':6,'correct':6,'minmul':1,'maxmul':7}
answers['iflong4'] = {'l':6,'correct':2,'minmul':1,'maxmul':6}
answers['iflong5'] = {'l':6,'correct':1,'minmul':1,'maxmul':5}
answers['iflong6'] = {'l':6,'correct':1,'minmul':1,'maxmul':4}
answers['ifflow1'] = {'l':6,'correct':2,'minmul':1,'maxmul':7}
answers['ifflow2'] = {'l':6,'correct':4,'minmul':1,'maxmul':7}
answers['ifflow3'] = {'l':6,'correct':7,'minmul':1,'maxmul':7}
answers['ifflow4'] = {'l':6,'correct':6,'minmul':1,'maxmul':7}
answers['ifflow5'] = {'l':6,'correct':1,'minmul':1,'maxmul':5}
answers['ifflow6'] = {'l':6,'correct':3,'minmul':1,'maxmul':7}
answers['ifflow7'] = {'l':6,'correct':6,'minmul':1,'maxmul':6}
answers['ifflow8'] = {'l':6,'correct':4,'minmul':1,'maxmul':6}
answers['ifflow9'] = {'l':6,'correct':5,'minmul':1,'maxmul':5}
answers['ifflow10'] = {'l':6,'correct':6,'minmul':1,'maxmul':7}
answers['ifflow11'] = {'l':6,'correct':6,'minmul':1,'maxmul':7}
answers['ifflow12'] = {'l':6,'correct':2,'minmul':1,'maxmul':7}
answers['ifflow13'] = {'l':6,'correct':2,'minmul':1,'maxmul':5}
answers['ifflow14'] = {'l':6,'correct':4,'minmul':1,'maxmul':8}
answers['filter1'] = {'l':6,'correct':4,'minmul':1,'maxmul':10}
answers['filter2'] = {'l':6,'correct':9,'minmul':1,'maxmul':10}
answers['filter3'] = {'l':6,'correct':2,'minmul':1,'maxmul':10}
answers['filter4'] = {'l':6,'correct':1,'minmul':1,'maxmul':5}
answers['filter5'] = {'l':6,'correct':4,'minmul':1,'maxmul':5}
answers['filter6'] = {'l':6,'correct':1,'minmul':1,'maxmul':5}
answers['filter7'] = {'l':6,'correct':2,'minmul':1,'maxmul':6}
answers['listmerge1'] = {'l':6,'correct':6,'minmul':1,'maxmul':7}
answers['listmerge2'] = {'l':6,'correct':4,'minmul':1,'maxmul':5}
answers['listmerge3'] = {'l':6,'correct':2,'minmul':1,'maxmul':8}
answers['anagrammer1'] = {'l':6,'correct':4,'minmul':1,'maxmul':6}
answers['anagrammer2'] = {'l':6,'correct':5,'minmul':1,'maxmul':6}
answers['anagrammer3'] = {'l':6,'correct':4,'minmul':1,'maxmul':8}
answers['anagrammer4'] = {'l':6,'correct':8,'minmul':1,'maxmul':8}

#7
answers['dict_type1'] = {'l':7,'correct':2,'minmul':1,'maxmul':6}
answers['dict_type2'] = {'l':7,'correct':3,'minmul':1,'maxmul':6}
answers['dict_parts1'] = {'l':7,'correct':3,'minmul':1,'maxmul':6}
answers['dict_parts2'] = {'l':7,'correct':7,'minmul':1,'maxmul':7}
answers['dict_parts3'] = {'l':7,'correct':5,'minmul':1,'maxmul':7}
answers['dict_index1'] = {'l':7,'correct':6,'minmul':1,'maxmul':7}
answers['dict_index2'] = {'l':7,'correct':6,'minmul':1,'maxmul':6}
answers['dict_index3'] = {'l':7,'correct':4,'minmul':1,'maxmul':8}
answers['dict_usage1'] = {'l':7,'correct':1,'minmul':1,'maxmul':4}
answers['dict_usage2'] = {'l':7,'correct':1,'minmul':1,'maxmul':4}
answers['dict_in1'] = {'l':7,'correct':3,'minmul':1,'maxmul':6}
answers['dict_in2'] = {'l':7,'correct':3,'minmul':1,'maxmul':6}
answers['dict_in3'] = {'l':7,'correct':1,'minmul':1,'maxmul':5}
answers['dict_in4'] = {'l':7,'correct':3,'minmul':1,'maxmul':5}
answers['dict_change1'] = {'l':7,'correct':1,'minmul':1,'maxmul':5}
answers['dict_change2'] = {'l':7,'correct':3,'minmul':1,'maxmul':5}
answers['dict_purpose1'] = {'l':7,'correct':2,'minmul':1,'maxmul':3}
answers['dict_purpose2'] = {'l':7,'correct':3,'minmul':1,'maxmul':3}
answers['dict_purpose3'] = {'l':7,'correct':2,'minmul':1,'maxmul':3}
answers['dict_purpose4'] = {'l':7,'correct':2,'minmul':1,'maxmul':3}
answers['dict_purpose5'] = {'l':7,'correct':3,'minmul':1,'maxmul':3}
answers['dict_of_lists1'] = {'l':7,'correct':1,'minmul':1,'maxmul':8}
answers['dict_of_lists2'] = {'l':7,'correct':4,'minmul':1,'maxmul':8}
answers['dict_of_lists3'] = {'l':7,'correct':1,'minmul':1,'maxmul':8}
answers['dict_of_lists4'] = {'l':7,'correct':7,'minmul':1,'maxmul':8}
answers['dict_of_lists5'] = {'l':7,'correct':6,'minmul':1,'maxmul':8}
answers['dict_of_dicts1'] = {'l':7,'correct':5,'minmul':1,'maxmul':10}
answers['dict_of_dicts2'] = {'l':7,'correct':4,'minmul':1,'maxmul':10}
answers['dict_of_dicts3'] = {'l':7,'correct':1,'minmul':1,'maxmul':10}
answers['dict_of_dicts4'] = {'l':7,'correct':3,'minmul':1,'maxmul':10}
answers['dict_of_dicts5'] = {'l':7,'correct':2,'minmul':1,'maxmul':10}
answers['dict_of_dicts6'] = {'l':7,'correct':5,'minmul':1,'maxmul':10}
answers['dict_looping1'] = {'l':7,'correct':4,'minmul':1,'maxmul':6}
answers['dict_looping2'] = {'l':7,'correct':5,'minmul':1,'maxmul':9}
answers['dict_looping3'] = {'l':7,'correct':2,'minmul':1,'maxmul':5}
answers['dict_looping4'] = {'l':7,'correct':5,'minmul':1,'maxmul':8}
answers['dict_looping5'] = {'l':7,'correct':4,'minmul':1,'maxmul':8}
answers['dict_looping6'] = {'l':7,'correct':5,'minmul':1,'maxmul':8}
answers['dicts_as_data1'] = {'l':7,'correct':4,'minmul':1,'maxmul':6}
answers['dicts_as_data2'] = {'l':7,'correct':1,'minmul':1,'maxmul':4}

#8
answers['function_basic1'] = {'l':8,'correct':6,'minmul':1,'maxmul':9}
answers['function_def1'] = {'l':8,'correct':1,'minmul':1,'maxmul':5}
answers['function_def2'] = {'l':8,'correct':4,'minmul':1,'maxmul':5}
answers['function_def3'] = {'l':8,'correct':4,'minmul':1,'maxmul':5}
answers['function_def4'] = {'l':8,'correct':3,'minmul':1,'maxmul':5}
answers['function_workings1'] = {'l':8,'correct':3,'minmul':1,'maxmul':5}
answers['function_workings2'] = {'l':8,'correct':7,'minmul':1,'maxmul':7}
answers['function_parts1'] = {'l':8,'correct':1,'minmul':1,'maxmul':5}
answers['function_parts2'] = {'l':8,'correct':1,'minmul':1,'maxmul':5}
answers['function_parts3'] = {'l':8,'correct':3,'minmul':1,'maxmul':5}
answers['function_usage1'] = {'l':8,'correct':10,'minmul':1,'maxmul':10}
answers['function_usage2'] = {'l':8,'correct':10,'minmul':1,'maxmul':10}
answers['function_usage3'] = {'l':8,'correct':1,'minmul':1,'maxmul':11}
answers['function_usage4'] = {'l':8,'correct':2,'minmul':1,'maxmul':8}
answers['function_usage5'] = {'l':8,'correct':2,'minmul':1,'maxmul':8}
answers['function_input1'] = {'l':8,'correct':2,'minmul':1,'maxmul':6}
answers['function_input2'] = {'l':8,'correct':2,'minmul':1,'maxmul':6}
answers['function_scope1'] = {'l':8,'correct':4,'minmul':1,'maxmul':4}
answers['function_scope2'] = {'l':8,'correct':4,'minmul':1,'maxmul':4}
answers['function_scope3'] = {'l':8,'correct':2,'minmul':1,'maxmul':4}
answers['turtle_nav1'] = {'l':8,'correct':4,'minmul':1,'maxmul':7}
answers['turtle_nav2'] = {'l':8,'correct':2,'minmul':1,'maxmul':7}
answers['turtle_nav3'] = {'l':8,'correct':5,'minmul':1,'maxmul':7}
answers['turtle_nav4'] = {'l':8,'correct':5,'minmul':1,'maxmul':6}
answers['turtle_thinking1'] = {'l':8,'correct':3,'minmul':1,'maxmul':5}
answers['turtle_thinking2'] = {'l':8,'correct':2,'minmul':1,'maxmul':7}
answers['turtle_thinking3'] = {'l':8,'correct':5,'minmul':1,'maxmul':10}
answers['turtle_function1'] = {'l':8,'correct':1,'minmul':1,'maxmul':6}
answers['turtle_function2'] = {'l':8,'correct':4,'minmul':1,'maxmul':5}
answers['turtle_function3'] = {'l':8,'correct':4,'minmul':1,'maxmul':9}
answers['turtle_function4'] = {'l':8,'correct':1,'minmul':1,'maxmul':6}
answers['turtle_function5'] = {'l':8,'correct':2,'minmul':1,'maxmul':6}
answers['turtle_refactor1'] = {'l':8,'correct':5,'minmul':1,'maxmul':8}





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
  answers[key]['entered'] = answer
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

def checkcheck(lesson):
  nCorrect = 0
  nTotal = 0
  for qid, q in answers.items():
    if q['l'] == lesson:
      nTotal += 1
      if 'entered' in q and q['correct'] == q['entered']:
        nCorrect += 1
      #else:
        #print( qid , q, lesson)
  return( nCorrect, nTotal )

if __name__ == "__main__":
  test = 6
  if test == 1:
    print( checkcheck(2) )
  elif test == 2:
    check('try_it_out', 8 )
    # Arithmetic
    check('leading_zero', 1 )
    check('big_numbers', 50000000000)
    check('arithmetic1', (3*4)+(5+6) )
    check('arithmetic2', (4*5)-(4-3) )
    check('spaces_in_arithmetic1', 4)
    check('spaces_in_arithmetic2', 3)
    check('parentheses', 1)
    # Modules
    check('notebook_blocks', 1)
    check('import_syntax1', 2)
    check('import_syntax2', 2)
    check('scientific_notation', 3)
    # Output
    check('code_blocks_output1', 3)
    check('code_blocks_output2', 3)
    check('code_blocks_output3', 7)
    check('code_blocks_output4', 5)
    check('code_blocks_output5', 5)
    # Variables
    check('variable_names1', 1)
    check('variable_names2', 1)
    check('variable_names3', 2)
    check('variable_names4', 1)
    check('variable_names5', 1)
    check('variable_names6', 1)
    check('variable_names7', 2)
    check('variable_names_cont1', 2)
    check('variable_names_cont2', 3)
    check('variable_assignment1', 5)
    check('variable_assignment2', 3)
    check('variable_assignment3', 2)
    check('variable_name_quality1', 3)
    check('reassignment1', 1)
    check('reassignment2', 2)
    check('reassignment3', 2)
    check('reassignment4', 1)
    check('reassignment5', 9)
    check('reassignment6', 5)
    check('reassignment7', 7)
    print( checkcheck(2) )
  elif test == 3:
    # Errors
    check('errors1', 4)
    # Type
    check('type1', 4)
    check('type2', 4)
    check('type3', 1)
    # Booleans
    check('booleans1', 2)
    check('booleans2', 4)
    check('booleans3', 1)
    # Strings
    check('writing_strings1', 'Hi Python')
    check('writing_strings2', 'abcdefghijklmnopqrstuvwxyz')
    check('string_length1', 3)
    check('string_length2', 7)
    check('string_length3', 0)
    check('string_length4', 4)
    check('quote_types1', 3)
    check('substrings_in_strings1', 4)
    check('substrings_in_strings2', 6)
    check('combining_strings1', 2)
    check('combining_strings2', 3)
    # Comparisons
    check('comparing_things1', 1)
    check('comparing_things2', 2)
    check('comparing_things3', 1)
    check('comparing_things4', 2)
    check('comparing_things5', 1)
    check('comparing_things6', 2)
    check('comparing_things7', 1)
    check('comparing_things8', 2)
    check('comparing_things9', 2)
    check('comparing_things10', 2)
    check('comparing_things11', 2)
    check('comparing_things12', 1)
    check('comparing_things13', 3)
    check('comparing_things14', 1)
    check('compare_v_assign1', 1)
    check('compare_v_assign2', 3)
    check('relative_comparisons1', 2)
    check('relative_comparisons2', 4)
    print( checkcheck(3) )
  elif test == 4:
    # Lists
    check('list_definitions1', [1,2,3])
    check('list_definitions2', ['1', '2', '3'])
    check('list_definitions3', 2)
    check('list_type1', 2)
    check('list_indexing1', 5)
    check('list_indexing2', 3)
    check('list_indexing3', 0)
    check('list_indexing4', 1)
    check('list_errors1', 6)
    check('list_changes1', 5)
    check('list_changes2', 5)
    check('list_edits1', 2)
    check('list_edits2', 2)
    check('list_edits3', 2)
    check('list_edits4', 3)
    check('list_edits5', 3)
    check('list_edits6', 2)
    check('list_edits7', 1 )
    check('list_edits8', 3)
    check('list_edits9', 1)
    check('list_edits10', 1)
    check('list_edits11', 2)
    check('list_edits12', 3)
    check('growing_lists1', 1)
    check('growing_lists2', 2)
    check('growing_lists3', 3)
    check('growing_lists4', 3)
    check('list_slicing1', 3)
    check('list_slicing2', 5)
    check('list_slicing3', 5)
    check('list_slicing4', 5)
    check('list_slicing5', 1)
    check('list_slicing6', 2)
    check('list_slicing7', 1)
    check('list_addition1', 6)
    check('list_addition2', 4)
    check('list_addition3', 6)
    check('empty_string1', 5)
    check('empty_string2', 3)
    check('empty_string3', 2)
    check('list_contents1', 4)
    check('list_contents2', 4)
    check('list_contents3', 2)
    check('list_contents4', 1)
    check('list_contents5', 2)
    check('list_contents6', 2)
    check('list_contents7', 1)
    check('list_contents8', 2)
    check('list_counts1', 4)
    check('list_counts2', 2)
    check('list_counts3', 6)
    check('list_counts4', 2)
    check('list_counts5', 6)
    check('list_summarizing1', 3)
    check('list_summarizing2', 18)
    check('list_summarizing3', 2)
    check('list_summarizing4', 1)
    check('list_transforming1', 1)
    check('list_transforming2', 2)
    check('list_transforming3', 2)
    check('list_transforming4', 3)
    check('list_transforming5', 3)
    print( checkcheck(4) )
  elif test == 5:
    check('loop1', 3)
    check('loop2', 6)
    check('loop3', 5)
    check('loop4', 4)
    check('loop5', 4)
    check('loop6', 3)
    check('loop7', 1)

    check('replace1', 3)
    check('replace2', 2)
    check('replace3', 1)
    check('growdata1', 4)
    check('growdata2', 5)
    check('growdata3', 4)
    check('growdata4', 2)

    check('forloop1', 5)
    check('forloop2', 5)
    check('forloop3', 5)
    check('forloop4', 4)
    check('forloop5', 1)
    check('forloop6', 1)
    check('forloop7', 3)
    print( checkcheck( 5 ))
  elif test == 6:
    check('loopcond1', 3), 4
    check('loopcond2', 2), 4
    check('loopcond3', 1), 1
    check('loopcond4', 4), 7
    check('loopcond5', 1), 3
    check('loopcond6', 3), 5
    check('loopcond7', 4), 4
    check('loopcond8', 7), 7
    check('iflong1', 6), 7
    check('iflong2', 7), 7
    check('iflong3', 6), 7
    check('iflong4', 2), 6
    check('iflong5', 1), 5
    check('iflong6', 1), 4
    check('ifflow1', 2), 7
    check('ifflow2', 4), 7
    check('ifflow3', 7), 7
    check('ifflow4', 6), 7
    check('ifflow5', 1), 5
    check('ifflow6', 3), 4
    check('ifflow7', 6), 6
    check('ifflow8', 4), 6
    check('ifflow9', 5), 5
    check('ifflow10', 6), 7
    check('ifflow11', 6), 7
    check('ifflow12', 2), 7
    check('ifflow13', 2), 5
    check('ifflow14', 4), 8
    check('filter1', 4), 10 
    check('filter2', 9), 10
    check('filter3', 2), 10
    check('filter4', 1), 5 
    check('filter5', 4), 5 
    check('filter6', 1), 5 
    check('filter7', 2), 6 
    check('listmerge1', 6), 7
    check('listmerge2', 4), 5
    check('listmerge3', 2), 8 
    check('anagrammer1', 4), 6
    check('anagrammer2', 5), 6
    check('anagrammer3', 4), 8
    check('anagrammer4', 8), 8
    print( checkcheck( 6 ))
  elif test == 7:
    check('dict_type1', 2), 6
    check('dict_type2', 3), 6
    check('dict_parts1', 3), 6
    check('dict_parts2', 7), 7
    check('dict_parts3', 5), 7
    check('dict_index1', 6), 7
    check('dict_index2', 6), 6
    check('dict_index3', 4), 8
    check('dict_usage1', 1), 4
    check('dict_usage2', 1), 4
    check('dict_in1', 3), 6
    check('dict_in2', 3), 6
    check('dict_in3', 1), 5
    check('dict_in4', 3), 5
    check('dict_change1', 1), 5
    check('dict_change2', 3), 5
    check('dict_purpose1', 2), 3 
    check('dict_purpose2', 3), 3
    check('dict_purpose3', 2), 3
    check('dict_purpose4', 2), 3
    check('dict_purpose5', 3), 3
    check('dict_of_lists1', 1), 8
    check('dict_of_lists2', 4), 8
    check('dict_of_lists3', 1), 8
    check('dict_of_lists4', 7), 8
    check('dict_of_lists5', 6), 8
    check('dict_of_dicts1', 5), 10
    check('dict_of_dicts2', 4), 10
    check('dict_of_dicts3', 1), 10
    check('dict_of_dicts4', 3), 10 
    check('dict_of_dicts5', 2), 10
    check('dict_of_dicts6', 5), 10
    check('dict_looping1', 4), 6 
    check('dict_looping2', 5), 9
    check('dict_looping3', 2), 5 
    check('dict_looping4', 5), 8 
    check('dict_looping5', 4), 8
    check('dict_looping6', 5), 8
    check('dicts_as_data1', 4), 6
    check('dicts_as_data2', 1), 4
    print( checkcheck( 7 ))
  elif test == 8:
      check('function_basic1', 6), 9
      check('function_def1', 1), 5
      check('function_def2', 4), 5
      check('function_def3', 4), 5
      check('function_def4', 3), 5
      check('function_workings1', 3), 5
      check('function_workings2', 7), 7
      check('function_parts1', 1), 5
      check('function_parts2', 1), 5
      check('function_parts3', 3), 1
      check('function_usage1', 10), 10
      check('function_usage2', 10), 10
      check('function_usage3', 1), 11
      check('function_usage4', 2), 8
      check('function_usage5', 2), 8
      check('function_input1', 2), 6
      check('function_input2', 2), 6
      check('function_scope1', 4), 4
      check('function_scope2', 4), 4 
      check('function_scope3', 2), 4
      check('turtle_nav1', 4), 7 
      check('turtle_nav2', 2), 7 
      check('turtle_nav3', 5), 7
      check('turtle_nav4', 5), 6
      check('turtle_thinking1', 3), 5 
      check('turtle_thinking2', 2), 7
      check('turtle_thinking3', 5), 10
      check('turtle_function1', 1), 6
      check('turtle_function2', 4), 5
      check('turtle_function3', 4), 9 
      check('turtle_function4', 1), 6
      check('turtle_function5', 2), 6
      check('turtle_refactor1', 5), 8
      print( checkcheck( 8 ))
