import os, shutil

# The path to home
home = os.path.expanduser('~')
# The path to desktop and Downloads
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
downloads = os.path.join(os.path.join(os.path.expanduser('~')), 'Downloads') 




############################################################################
#### CODE TO ORGANISE THE FILES IN DESKTOP #################################
#############################################################################






####################
# This function is to check if a diretory exist or not.
# If doesn't exist it will create one
def check_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


####################
# To check if a file with some name already exist or not
# If it has same name it will keep renaming it by adding '_1' to it until it has a unique name
# This will help in avoiding errors caused by same name
# the function is recursive
##################
# file_path is the path that we want to be unique(or available)
# new_path is path(or the renamed file) that will be allocated to file_path to make file_path free
def check_file(file_path, new_path):
	# rename when new_path is available to rename and file_path exists
	# this will rename file_path to new_path
	if not os.path.exists(new_path):
		if os.path.exists(file_path):
			os.rename(file_path, new_path)
	else:
		# when file_name is occupied
		# Add '_1' to the name and again check if this file name exist
		file_dir = os.path.dirname(new_path)
		file_name, file_extension = os.path.splitext(os.path.basename(new_path))
		file_name = str(file_name) + "_1" + str(file_extension)
		new_path = os.path.join(file_dir, file_name)
		check_file(file_path, new_path)


#####################
# This function is to clean a specified directory
def clean_path(path):
	for p in os.listdir(path):
		if os.path.isdir(p) and p!="FILE_ORGANISED":
			shutil.rmtree(p)


def rename_dir():
	for p in os.listdir(desktop):
		if p=="FILE_ORGANISED":
			os.rename(p, os.path.join(desktop, "FILE_ORGANISED_2"))


###################
# The main line of codes to organise the files
# In a specific directory go through all the files in the folders and subfolders and so on in it.
# Ignore the main scipt file('script.py')
# Now check the extension of the file and if there is no specific folder for these category file reate one
# Then check if there is another file with same name as current one in case rename that.
# finally move the file to its specific folder

def Organise_desktop():
	rename_dir()
	for dirpath, dirs, files in os.walk(desktop):	
		for filename in files:
			fname = os.path.join(dirpath,filename)

			if fname==os.path.join(downloads, "script.py"):
				continue

			file_name, file_extension = os.path.splitext(fname)
			dir_to_check = os.path.join(os.path.join(desktop, "FILE_ORGANISED/"), os.path.join(file_extension[1:].lower(), "test.test"))
			directory = os.path.dirname(dir_to_check)
			check_dir(directory)

			new_path = os.path.join(directory, os.path.basename(fname))
			check_file(new_path, new_path)
			shutil.move(fname, new_path)


	# Finally clean the main directory and get rid of unnecessary folders
	clean_path(desktop)

Organise_desktop()




############################################################################
#### CODE TO FIND TOP 10 BIGGEST FILE IN THE COMPUTER ######################
#############################################################################



def top_files():
	sizearray = []

	for dirpath, dirs, files in os.walk(home):	
		for filename in files:
			fname = os.path.join(dirpath,filename)
			sizearray.append([os.path.getsize(fname), fname])

	sizearray.sort(reverse=True)

	for i in sizearray[:10]:
		print "File path : " + str(i[1]) + "    -     size: " +  str(i[0]) + " bytes"

top_files()


		





