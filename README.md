The test was a part of automatization test course. The test uses Selenium WebDriver and PyTest and implements Singleton and PageObject patterns.

Test scenario:
1) Open main page http://cars.com
2) Open tab "Read Spec & Reviews"
3) Select random car characteristics
4) On Trim tab click to link "[Car model name] trim comparison"
5) Remember first trim characteristics (Engines, Transmissions)
6) Repeat steps 1-5 for another car
7) Click on Research car link
8) Click on Side-by-side Comparisons
9) Select first remembered car
10) Use 'Add another car' and select second rememebered car
11) Check characteristics on compare page
