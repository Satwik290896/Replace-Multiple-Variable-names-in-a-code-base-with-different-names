# Python: Replace-Multiple-Variable-names-in-a-code-base-with-different-names

A python script which would replace “MACROs/API_names/any other functionality names” with “the given/required names”.
This can reduce any effort required and can be replaced with a quick short run

Command line format:
   “python Modify_MACROs.py <Location of code_base_folder> <Subfolder_name_that need_cleanup> <number_of_Replacements (integer)>
<Old_MACRO_1_name> <new_MACRO_1_name> <Old_MACRO_2_name> <new_MACRO_2_name> ……”

//Command line Arguments
1.	"Location of code_base_folder" 
2.	<Subfolder_name_that need_cleanup>  - Module name should be the “sub folder name” in the location given
3.	<number_of_Replacements (integer)>  - Integer needs to be give 
4.	<Old_MACRO_1_name>    - Replacement 1
5.	<new_MACRO_1_name>
6.	<Old_MACRO_2_name>    - Replacement 2
7.	<new_MACRO_2_name>
8.	.
9.	.
10.	.
11.	.

Warnings to take note of in using the script:
-	The code might change the definitions of the MACROs as well. 
If u want old MACRO definition to be present, please do manually. The same will apply to API/functionality names as well

Make Sure to allot some memory space in the "Location of code_base_folder"
