# dictionary of books and thier available copies
books = {
	'Harry Potter': 2,
	'To kill a Mockingbird': 5,
	'Pride and Prejudice': 0,
	'The great Gatsby': 8,
	'1984': 8, 
}
#display book availability and warning on low stock
for book, copies in books.items():
	print(f"'{book}': {copies} copies available")
	if copies <= 2:
		print(f"Warning: Low stock on '{book}'!")