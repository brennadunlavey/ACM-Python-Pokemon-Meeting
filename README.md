# ACM-Python-Pokemon-Meeting

This repostitory is for use by OHIO ACM for our meeting "Learn Python With Pokemon".

In this meeting, we are utilizing the [Pokedex API](https://pokeapi.co/) to explore the basics of Python and its applications in data science. 

There are two main endpoints that we are accessing data from with the API: "pokemon" and "pokemon-species". The `data-examples` directory shows the data returned from each of these endpoints for the "pikachu" entry, as well as a file with combined data, and .simple files with bulky data removed. 

The file `poke_mod.py` contains the very useful function `loadPokemon()`, which allows you to make API calls for a given amount of pokemon from one or both of the used endpoints, and opt to save data locally. To use the function, import the file in your code with `import poke_mod`. The recommended basic use of the loadPokemon function is `poke_mod.loadPokemon(10,updateCache=True,loadFromCache=True)`. This will return a list of the first 10 Pokemon, save the data to json-cache/PokemonSpecies.json, and access it from that file if it has already run. Once you have a solid plan for proccessing data, load more than 10 to get a better view of the data.

There is a lot of data available for each Pokemon entry. The following values may be considered specific points of interest:
- base_happiness
- base_experience
- weight 
- height
- habitat
- stats
- types 
- capture_rate 
- egg_groups 
- shape 
- abilities 
- moves 

Try to come up with cool ways to analyze and process the data from the API. Below are some basic ideas to start with:
- Each Pokemon has a habitat it is from. How does the habitat affect the Pokemon that live in it? For example, which one has the highest average happiness rates?
- How can you create a scatter plot to graph each pokemon on axes of two different values? For example, what combinations of weight and height are present?
- What happens when Pokemon evolve? What values tend to change the most? How long are evolution chains?
- It's always important to make data easy to browse and view. Programmaticaly make a markdown file that shows important information on each Pokemon, such as name, types, stats, and a picture. 
- There are complicated relationships and groupings among pokemon. How can you create associations and display them in a network graph to gain information about these relationships?


### Code Examples 

Basic examples of how to approach these ideas are available in the `code-examples` directory. To try out these programs, run them from this root directory (for example, run `python code-examples/using-objects.py`). You may need to use pip to install libraries for some of the examples (for example, you may need to run `pip install matplotlib` to run network.py). You will also need to create an `outputs/` directory within the `code-examples/` folder, for the programs to place output files in.
