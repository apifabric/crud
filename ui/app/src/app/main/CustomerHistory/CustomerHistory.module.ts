import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {CUSTOMERHISTORY_MODULE_DECLARATIONS, CustomerHistoryRoutingModule} from  './CustomerHistory-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    CustomerHistoryRoutingModule
  ],
  declarations: CUSTOMERHISTORY_MODULE_DECLARATIONS,
  exports: CUSTOMERHISTORY_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class CustomerHistoryModule { }