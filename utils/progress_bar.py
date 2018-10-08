from progressbar import Percentage, ProgressBar, Bar, ETA

widgets = [Percentage(), ' ', Bar(), ' ', ETA()]
progress = ProgressBar(widgets=widgets)
