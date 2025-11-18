"""Heaper - A heap-based to-do list manager."""

import heapq
import json
import os
from pathlib import Path
from typing import List, Optional

from .todo import ToDo


class Heaper:
    """A heap-based to-do list manager."""
    
    def __init__(self, storage_path: Optional[str] = None):
        """Initialize the Heaper.
        
        Args:
            storage_path: Path to the storage file. If None, uses default.
        """
        if storage_path is None:
            storage_path = os.path.expanduser("~/.heaper.json")
        self.storage_path = Path(storage_path)
        self.heap: List[tuple] = []
        self.load()
    
    def load(self):
        """Load the heap from storage."""
        if self.storage_path.exists():
            try:
                with open(self.storage_path, 'r') as f:
                    data = json.load(f)
                    # Convert loaded data back to heap structure
                    # Each item is [priority, content]
                    for item in data:
                        self.heap.append((item['prio'], item['content']))
                    heapq.heapify(self.heap)
            except (json.JSONDecodeError, KeyError):
                # If file is corrupted, start with empty heap
                self.heap = []
    
    def save(self):
        """Save the heap to storage."""
        data = [{'prio': prio, 'content': content} for prio, content in self.heap]
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.storage_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def push(self, priority: int, content: str):
        """Add an item to the heap.
        
        Args:
            priority: Priority value (lower is higher priority)
            content: The to-do item content
        """
        heapq.heappush(self.heap, (priority, content))
        self.save()
    
    def pop(self) -> Optional[tuple]:
        """Remove and return the highest priority item.
        
        Returns:
            Tuple of (priority, content) or None if heap is empty
        """
        if not self.heap:
            return None
        item = heapq.heappop(self.heap)
        self.save()
        return item
    
    def peek(self, show_all: bool = False) -> List[tuple]:
        """View items in the heap.
        
        Args:
            show_all: If True, return all items sorted by priority.
                     If False, return only the highest priority item.
        
        Returns:
            List of tuples (priority, content)
        """
        if not self.heap:
            return []
        
        if show_all:
            return sorted(self.heap)
        else:
            return [self.heap[0]]
    
    def is_empty(self) -> bool:
        """Check if the heap is empty."""
        return len(self.heap) == 0
