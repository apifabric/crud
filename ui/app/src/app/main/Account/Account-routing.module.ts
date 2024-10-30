import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AccountHomeComponent } from './home/Account-home.component';
import { AccountNewComponent } from './new/Account-new.component';
import { AccountDetailComponent } from './detail/Account-detail.component';

const routes: Routes = [
  {path: '', component: AccountHomeComponent},
  { path: 'new', component: AccountNewComponent },
  { path: ':id', component: AccountDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Account-detail-permissions'
      }
    }
  },{
    path: ':account_id/Transaction', loadChildren: () => import('../Transaction/Transaction.module').then(m => m.TransactionModule),
    data: {
        oPermission: {
            permissionId: 'Transaction-detail-permissions'
        }
    }
}
];

export const ACCOUNT_MODULE_DECLARATIONS = [
    AccountHomeComponent,
    AccountNewComponent,
    AccountDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AccountRoutingModule { }