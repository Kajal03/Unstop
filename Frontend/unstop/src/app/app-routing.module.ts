import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { BookTicketComponent } from './components/book-ticket/book-ticket.component';

const routes : Routes = [
  {
    path: '',
    component: HomeComponent
  },
  {
    path: 'book-ticket',
    component: BookTicketComponent
  }
]

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
