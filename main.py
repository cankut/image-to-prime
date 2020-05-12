from PrimeSearcher import PrimeSearcher

###

ps = PrimeSearcher("./images/euler.jpg")
ps.rescale(60*60, fit_to_original=True)
ps.search(max_iterations=1000, noise_count=1, break_on_find=False)
    


