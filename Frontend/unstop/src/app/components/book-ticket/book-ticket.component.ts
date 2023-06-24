import { Component } from '@angular/core';
import { Title } from '@angular/platform-browser';

@Component({
  selector: 'app-book-ticket',
  templateUrl: './book-ticket.component.html',
  styleUrls: ['./book-ticket.component.css']
})
export class BookTicketComponent {

  constructor(private titleService: Title){}

  ngOnInit(): void {
    this.titleService.setTitle('Book Ticket')
  }
  
}
