"""ToDo class for heaper."""

import json


class ToDo:
    """A to-do item with priority and content."""
    
    def __init__(self, prio, content):
        """Initialize a ToDo item.
        
        Args:
            prio: Priority value (lower is higher priority)
            content: The to-do item content
        """
        self.prio = prio
        self.content = content
    
    def __str__(self):
        """Return string representation of the to-do item."""
        return "[{}] {}".format(self.prio, self.content)
    
    def to_json(self):
        """Convert to JSON string.
        
        Returns:
            JSON string representation
        """
        return json.dumps({
            "prio": self.prio,
            "content": self.content
        })
    
    @classmethod
    def from_json(cls, json_str):
        """Create a ToDo from JSON string.
        
        Args:
            json_str: JSON string containing prio and content
            
        Returns:
            ToDo instance
        """
        d = json.loads(json_str)
        return cls(d["prio"], d["content"])
