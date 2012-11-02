# This is how you declare a class in python
# The thing in parentheses is what CelestialCatalog inherits from
# (it inherits from "dict", which is a built-in data type in python,
# just like a hash in IDL)
class CelestialCatalog(dict):
    """
    A Celestial Catalog!
    """
    pass



# A Class with no inheritance, it is just an object
class CelestialCatalogEntry(object):
    """
    Celestial Catalog Entry - could be a star or a galaxy or a nebula or
    anything celestial
    """
    def __init__(self,ra=None,dec=None,vmag=None,name=None):
        """
        Initialization for a new class

        The defaults are all None, so you have to specify them

        Example:
        >>> CalabashNebula = CelestialCatalogEntry(ra=115.57013,dec=-14.71447,9.47,name='CalabashNebula')
        >>> CalabashNebula.ra
            115.57013
        """
        # Set the class vmag and name to be the input values
        # the underscore self._vmag indicates that it is "private"
        # (though you still could modify it if you tried)
        self._vmag = vmag
        self._name = name

        # With these lines, we set a "default" that is None,
        # but also set the value.  
        self._ra = None
        # self.ra = ra calls the ra.setter code below, which
        # is important because it checks that RA is "in bounds"
        self.ra = ra
        self._dec = None
        self.dec = dec

    # We define "setters" and "getters" as class properties
    # As long as we only define this property, RA is read-only
    @property
    def ra(self):
        return self._ra

    # however, we can make the "fields" writeable only if they are None,
    # the default:
    @ra.setter
    def ra(self, value):
        if value < 0 or value > 360:
            raise ValueError("RA is out of range, it must be between 0 and 360 deg")
        if self._ra is None:
            self._ra = value

    @property
    def dec(self):
        return self._dec

    @dec.setter
    def dec(self, value):
        if value < -90 or value > 90:
            raise ValueError("Dec is out of range, it must be between 0 and 360 deg")
        if self._dec is None:
            self._dec = value

    @property
    def vmag(self):
        return self._vmag

    @vmag.setter
    def vmag(self, value):
        if self._vmag is None:
            self._vmag = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if self._name is None:
            self._name = value

# A class that inherits from CelestialCatalogEntry
class StarCatalogEntry(CelestialCatalogEntry):
    """
    Stars have additional properties, like spectral type
    """
    def __init__(self, sptype=None, **kwargs):
        """
        Stars have an extra property, so they must have an extra init keyword
        BUT, we don't want to repeat all that old code, so we accept a
        "dictionary of keywords", which means unlimited additional keywords
        """
        # this cryptic little bit called "super" is a "magic" way to do class
        # inheritance stuff.  It basically says, 'Run the __init__ function from
        # all of the classes I inherit from'.  The **kwargs here means that all
        # arguments not explicitly taken by THIS function (i.e., any arguments passed
        # that are not sptype) get passed on to StarCatalogEntry.__init__
        super(StarCatalogEntry,self).__init__(**kwargs)
        self._sptype = sptype

    @property
    def sptype(self):
        return self._sptype

    @sptype.setter
    def sptype(self, value):
        if self._sptype is None:
            self._sptype = value

    # Now here's the really neat bit.  Overloading.
    # When you "print" something in python, it actually calls the objects __str__ function
    # You might ask, "but what if I printed a number, not an object?"
    # In python, everything's an object.  It's trippy but awesome.
    def __str__(self):
        """ 
        This function gets called whenever a StarCatalogEntry is printed
        """
        # python has some cool string formatting features too
        return "Star {0} is at ra,dec {1},{2} with vmag={3} and sptype={4}".format(
                self._name, self._ra, self._dec, self._vmag, self._sptype)


# Now things get really interesting and complicated
# What if we make a list of stars
# stars = [star1,star2,star3]
# but what we really want is the magnitudes of those stars?
# stars.vmag won't work, BUT we can MAKE it work!
#
# We'll make our CelestialCatalog inherit from list, so it will
# be a list with extra features
class CelestialCatalog(list):
    # we won't override list's init, we'll just leave that alone

    @property
    def vmag(self):
        """
        Get the vmag nitudes of all Stars in the CelestialCatalog
        """
        # this is called a "list comprehension".  
        return [star.vmag for star in self]
        # Explain in your own words (right here) what this line is doing 





if __name__ == "__main__":
    """ This code gets executed if you run the StarCatalog code:
    python StarCatalog.py
    In [1]: %run StarCatalog.py
    """
    Rigel = StarCatalogEntry(name='Rigel', vmag=0.12, sptype='B8Iab', ra=78.634467, dec=-8.201638)
    Betelgeuse = StarCatalogEntry(name='Betelgeuse', vmag=0.42, sptype='M2Iab', ra=88.792939, dec=7.407064)
    #Theta1c = StarCatalogEntry(name='Theta1COri', vmag=5.13, sptype='O4-6pv', ra=, dec=)
    Altair = StarCatalogEntry(name='Altair', vmag=0.77, sptype='A7V', ra=297.695827, dec=8.868321)

    stars = CelestialCatalog((Rigel,Betelgeuse,Altair))
