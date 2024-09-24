# Output to markdown files to make documentation

# open a file
myDocs = open('code-examples/outputs/my-docs.md', 'w')

# use the write function to write to the file
# note: newline characters (\n) need included with write, and markdown needs two newlines for it to display one
myDocs.write('# Sample Documentation\n\n')
myDocs.write('You can display images from local files:\n\n')
myDocs.write('![Network graph](../materials/network.png)\n\n')

# "#" characters make headers
myDocs.write('### You can make headers of different sizes\n\n')

myDocs.write('You can also display images from the web:\n\n')
myDocs.write('![ACM logo](https://upload.wikimedia.org/wikipedia/commons/8/8e/Association_for_Computing_Machinery_%28ACM%29_logo.svg)\n\n')

myDocs.close()

print('Check out code-examples/outputs/my-docs.md!')
print('Open in preview mode to view everything properly')
