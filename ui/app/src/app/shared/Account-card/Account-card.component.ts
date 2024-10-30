import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Account-card.component.html',
  styleUrls: ['./Account-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Account-card]': 'true'
  }
})

export class AccountCardComponent {


}