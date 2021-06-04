# pokemon-xml-data

An extraction and conversion tool that obtains pokemon species and move data from [pokeapi.co](pokeapi.co) and converts it to XML.

This small tool was used to obtain and provide data for the project LPOOmon, created for LPOO. The main focus was getting the job done in a timely fashion so there was very little to no effort put into making clean code.

## Usage

Firstly adjust `config.py` to suit your needs, it has the following format:
```python
GENERATION = 1
LANGUAGE = 'en'
VERSION = 'yellow'
```

Where 
  * `GENERATION` can be a integer from 1 through 8 (As of the time of writing)
  * `LANGUAGE` is a valid language name (Any entry from [this list](https://pokeapi.co/api/v2/language/)) 
  * `VERSION` is a valid game version name (Any entry from [this list](https://pokeapi.co/api/v2/version-group/))
 
After the configuration is concluded just run

```sh
python3 main.py
```

The program should start downloading the data straight away, this process may take a few minutes depending on the generation.

After it's concluded two files `species.xml` and `moves.xml` should have been created with the following formats:

**`species.xml`**:

```xml
<species>
  <_1> // 1 is the Pokemon's id
    <base_exp>64</base_exp>
    <moves>
      <_22>13</_22> // Format: <_moveId>levelLearntAt</_moveId>
      <_33>1</_33>
      <_45>1</_45>
      <_73>7</_73>
      <_74>34</_74>
      <_75>27</_75>
      <_76>48</_76>
      <_77>20</_77>
      <_79>41</_79>
    </moves>
    <name>bulbasaur</name>
    <stats>
      <attack>49</attack>
      <defense>49</defense>
      <hp>45</hp>
      <special-attack>65</special-attack>
      <special-defense>65</special-defense>
      <speed>45</speed>
    </stats>
  </_1>
...
</species>
```

**`moves.xml`**   
```xml
<moves>
  ...
  <_10> // 10 is the Move's id
      <accuracy>100</accuracy>
      <description>Scratches with sharp claws.</description>
      <name>Scratch</name>
      <power>40</power>
      <pp>35</pp>
  </_10>
...
</moves>
```
