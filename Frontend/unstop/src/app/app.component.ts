import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'unstop';
  constructor(private router: Router) {}

  showGetStarted() {
    if(this.router.url == '/'){
      return true;
    }
    return false;
  }
}
