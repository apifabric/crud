import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './CustomerHistory-card.component.html',
  styleUrls: ['./CustomerHistory-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.CustomerHistory-card]': 'true'
  }
})

export class CustomerHistoryCardComponent {


}