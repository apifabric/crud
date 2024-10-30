import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CustomerHistoryHomeComponent } from './home/CustomerHistory-home.component';
import { CustomerHistoryNewComponent } from './new/CustomerHistory-new.component';
import { CustomerHistoryDetailComponent } from './detail/CustomerHistory-detail.component';

const routes: Routes = [
  {path: '', component: CustomerHistoryHomeComponent},
  { path: 'new', component: CustomerHistoryNewComponent },
  { path: ':id', component: CustomerHistoryDetailComponent,
    data: {
      oPermission: {
        permissionId: 'CustomerHistory-detail-permissions'
      }
    }
  }
];

export const CUSTOMERHISTORY_MODULE_DECLARATIONS = [
    CustomerHistoryHomeComponent,
    CustomerHistoryNewComponent,
    CustomerHistoryDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CustomerHistoryRoutingModule { }